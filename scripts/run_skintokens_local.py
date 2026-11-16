"""Run the public SkinTokens implementation locally without Gradio or HF inference."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import signal
import sys
import time
from pathlib import Path


ROOT = Path(os.environ.get("SKINTOKENS_LOCAL_ROOT", Path(__file__).resolve().parent)).resolve()
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))

import torch  # noqa: E402

import demo  # noqa: E402


MODEL_CKPT = "experiments/articulation_xl_quantization_256_token_4/grpo_1400.ckpt"

PROFILES = {
    "nopost": {
        "top_k": 5,
        "top_p": 0.95,
        "temperature": 1.0,
        "repetition_penalty": 2.0,
        "use_postprocess": False,
    },
    "conservative": {
        "top_k": 20,
        "top_p": 0.90,
        "temperature": 0.70,
        "repetition_penalty": 1.5,
        "use_postprocess": True,
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_one(item: dict, defaults: argparse.Namespace) -> dict:
    profile_name = item.get("profile")
    profile = PROFILES.get(profile_name, {})
    if profile_name is not None and not profile:
        raise ValueError(f"Unknown profile {profile_name!r}; expected one of {sorted(PROFILES)}")

    mesh = Path(item["mesh"]).resolve()
    output = Path(item["output"]).resolve()
    if not mesh.is_file():
        raise FileNotFoundError(mesh)
    output.parent.mkdir(parents=True, exist_ok=True)

    parameters = {
        "beams": int(item.get("beams", defaults.beams)),
        "top_k": int(item.get("top_k", profile.get("top_k", defaults.top_k))),
        "top_p": float(item.get("top_p", profile.get("top_p", defaults.top_p))),
        "temperature": float(item.get("temperature", profile.get("temperature", defaults.temperature))),
        "repetition_penalty": float(
            item.get("repetition_penalty", profile.get("repetition_penalty", defaults.repetition_penalty))
        ),
        "use_skeleton": bool(item.get("use_skeleton", defaults.use_skeleton)),
        "use_transfer": bool(item.get("use_transfer", not defaults.no_transfer)),
        "use_postprocess": bool(item.get("use_postprocess", profile.get("use_postprocess", defaults.postprocess))),
    }

    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()
        torch.cuda.synchronize()
    started = time.perf_counter()
    demo.run_rig(
        [mesh],
        parameters["top_k"],
        parameters["top_p"],
        parameters["temperature"],
        parameters["repetition_penalty"],
        parameters["beams"],
        parameters["use_skeleton"],
        parameters["use_transfer"],
        parameters["use_postprocess"],
        [output],
        MODEL_CKPT,
        None,
    )
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    finished = time.perf_counter()

    if not output.is_file() or output.stat().st_size == 0:
        raise RuntimeError(f"SkinTokens did not create a non-empty output: {output}")

    report = {
        "status": "ok",
        "profile": profile_name,
        "input": str(mesh),
        "output": str(output),
        "output_bytes": output.stat().st_size,
        "output_sha256": sha256(output),
        "timing_seconds": {"mesh_process_export": finished - started},
        "peak_cuda_bytes": torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0,
        "parameters": parameters,
        "model_ckpt": MODEL_CKPT,
    }
    metrics_path = Path(item.get("metrics_output") or output.with_suffix(".local_metrics.json")).resolve()
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("SKINTOKENS_LOCAL_ITEM " + json.dumps(report), flush=True)
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mesh", nargs="?")
    parser.add_argument("--output")
    parser.add_argument("--manifest", help="JSON list of mesh/output/profile objects")
    parser.add_argument("--postprocess", action="store_true")
    parser.add_argument("--use-skeleton", action="store_true")
    parser.add_argument("--no-transfer", action="store_true")
    parser.add_argument("--beams", type=int, default=20, choices=range(1, 21))
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--top-p", type=float, default=0.95)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--repetition-penalty", type=float, default=2.0)
    parser.add_argument("--metrics-output")
    parser.add_argument("--continue-on-error", action="store_true")
    args = parser.parse_args()

    if bool(args.manifest) == bool(args.mesh):
        parser.error("provide exactly one of mesh or --manifest")
    if args.mesh and not args.output:
        parser.error("--output is required with mesh")

    if args.manifest:
        manifest_path = Path(args.manifest).resolve()
        items = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(items, list) or not items:
            raise ValueError("manifest must contain a non-empty JSON list")
    else:
        items = [{"mesh": args.mesh, "output": args.output}]

    total_started = time.perf_counter()
    server_proc = demo.start_bpy_server()
    try:
        server_started = time.perf_counter()
        demo.wait_for_bpy_server(timeout=60)
        server_ready = time.perf_counter()

        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
            torch.cuda.synchronize()
        load_started = time.perf_counter()
        demo.load_model(MODEL_CKPT, None)
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        load_finished = time.perf_counter()

        reports = []
        for index, item in enumerate(items):
            item_started = time.perf_counter()
            try:
                reports.append(run_one(item, args))
            except Exception as exc:
                failure = {
                    "status": "error",
                    "index": index,
                    "profile": item.get("profile"),
                    "input": str(Path(item.get("mesh", "")).resolve()),
                    "output": str(Path(item.get("output", "")).resolve()),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "timing_seconds": {"until_error": time.perf_counter() - item_started},
                    "model_ckpt": MODEL_CKPT,
                }
                reports.append(failure)
                print("SKINTOKENS_LOCAL_ITEM " + json.dumps(failure), flush=True)
                if not args.continue_on_error:
                    raise
        rig_finished = time.perf_counter()
    finally:
        if server_proc.poll() is None:
            os.killpg(os.getpgid(server_proc.pid), signal.SIGTERM)
            try:
                server_proc.wait(timeout=10)
            except Exception:
                os.killpg(os.getpgid(server_proc.pid), signal.SIGKILL)

    report = {
        "status": "ok" if all(item["status"] == "ok" for item in reports) else "partial",
        "item_count": len(reports),
        "ok_count": sum(item["status"] == "ok" for item in reports),
        "error_count": sum(item["status"] != "ok" for item in reports),
        "timing_seconds": {
            "bpy_server_start": server_ready - server_started,
            "model_load": load_finished - load_started,
            "all_items": rig_finished - load_finished,
            "model_load_plus_all_items": rig_finished - load_started,
            "wall_total": rig_finished - total_started,
        },
        "model_ckpt": MODEL_CKPT,
        "items": reports,
    }
    if args.metrics_output:
        metrics_path = Path(args.metrics_output).resolve()
    elif args.manifest:
        metrics_path = Path(args.manifest).resolve().with_suffix(".summary.json")
    else:
        metrics_path = Path(args.output).resolve().with_suffix(".local_summary.json")
    metrics_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("SKINTOKENS_LOCAL_RESULT " + json.dumps(report))
    return 0 if report["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
