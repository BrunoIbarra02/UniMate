#!/usr/bin/env python3
"""Build a deterministic quad10 structural-QA and rig-freeze manifest.

The script deliberately consumes existing Blender audit JSON instead of opening
the binary assets.  Rig identity, annotation validation, and canonical-facing
results are captured in the source metadata produced on the inference host.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


AUDIT_PROFILE_RE = re.compile(r"^(?P<profile>.+?)-an_object_.*-rep_(?P<rep>\d+)-\d+$")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--audit-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    plan = load_json(args.plan)
    metadata = load_json(args.metadata)
    thresholds = plan["thresholds"]
    audits: dict[str, list[dict]] = {}
    for path in sorted(args.audit_dir.glob("*.json")):
        match = AUDIT_PROFILE_RE.match(path.stem)
        if match:
            report = load_json(path)
            report["_file"] = path.name
            report["_rep"] = int(match.group("rep"))
            audits.setdefault(match.group("profile"), []).append(report)

    results = []
    for item in plan["profiles"]:
        profile = item["profile"]
        source = metadata[profile]
        canonical = source["canonical_gate"]
        annotation = source["annotation_validation"]
        profile_audits = sorted(audits.get(profile, []), key=lambda row: row["_rep"])
        failures = []

        if not annotation.get("accepted") or annotation.get("issues"):
            failures.append("canonical_bone_annotation")
        if annotation.get("generic_bone_count") != 0:
            failures.append("generic_bones_remain")
        if not canonical.get("accepted") or canonical.get("issues"):
            failures.append("canonical_conditioning")
        if not canonical.get("face_left") or not canonical.get("face_right"):
            failures.append("facing_pair_missing")
        if canonical.get("forward_margin", 0.0) < thresholds["forward_margin_min"]:
            failures.append("facing_margin")
        if len(profile_audits) != thresholds["required_repetitions"]:
            failures.append("audit_repetition_count")

        max_edge = max((row["edge_stretch_max"] for row in profile_audits), default=None)
        max_edge_p99 = max((row["edge_stretch_p99_max"] for row in profile_audits), default=None)
        min_leg_fraction = min(
            (
                row["moving_leg_bone_count_5deg"] / max(row["leg_bone_count"], 1)
                for row in profile_audits
            ),
            default=None,
        )
        if max_edge is None or max_edge > thresholds["edge_stretch_max"]:
            failures.append("severe_edge_tearing")
        if max_edge_p99 is None or max_edge_p99 > thresholds["edge_stretch_p99_max"]:
            failures.append("distributed_edge_tearing")
        if min_leg_fraction is None or min_leg_fraction < thresholds["moving_leg_fraction_min"]:
            failures.append("insufficient_leg_activity")

        passed = not failures
        digest = source["rig_sha256"]
        results.append(
            {
                "species": item["species"],
                "profile": profile,
                "status": "pass" if passed else "blocked",
                "failures": failures,
                "rig": {
                    "sha256": digest,
                    "size": source["rig_size"],
                    "source": source["remote_path"],
                    "version": f"{plan['release_id']}+sha256.{digest[:12]}" if passed else None,
                    "frozen_uri": item["frozen_uri"].format(sha256=digest) if passed else None,
                },
                "canonicalization": {
                    "joint_count": annotation.get("joint_count"),
                    "generic_bone_count": annotation.get("generic_bone_count"),
                    "review_mode": annotation.get("review_mode"),
                },
                "facing": {
                    "left": canonical.get("face_left"),
                    "right": canonical.get("face_right"),
                    "forward_margin": canonical.get("forward_margin"),
                },
                "animation_metrics": {
                    "repetitions": len(profile_audits),
                    "edge_stretch_max": max_edge,
                    "edge_stretch_p99_max": max_edge_p99,
                    "moving_leg_fraction_min": min_leg_fraction,
                    "audit_files": [row["_file"] for row in profile_audits],
                },
            }
        )

    output = {
        "schema": "unimate.quad10-release-qa/1",
        "release_id": plan["release_id"],
        "thresholds": thresholds,
        "summary": {
            "total": len(results),
            "passed": sum(row["status"] == "pass" for row in results),
            "blocked": sum(row["status"] == "blocked" for row in results),
        },
        "profiles": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output["summary"], sort_keys=True))
    for row in results:
        print(f"{row['species']}: {row['status']} ({row['profile']})", *row["failures"])
    return 0 if output["summary"]["blocked"] == plan.get("expected_blocked", 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
