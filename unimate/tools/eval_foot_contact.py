"""Automated foot-slide / ground-penetration QA sweep for generated clips.

Replaces the current review process for ``unimate.inference.sample`` output —
watching the per-clip ``_fk.mp4`` renders written by
``unimate.utils.visualization.visualize_and_save_motions`` and eyeballing
whether feet skate or sink into the ground — with a metric computed over
every ``.npy`` motion feature file in a samples directory.

Pipeline, per clip:
  1. Resolve ``object_type`` from the filename (same ``'-'``-prefix rule as
     ``data_process/mesh_animation/animate_motion.py::resolve_object_type``)
     and look up its skeleton in one of the dataset ``cond.npy`` files.
  2. Recover global joint positions via FK
     (``unimate.utils.motion_utils.recover_unimate_joint_pos_from_rot``,
     the same call ``visualize_and_save_motions`` uses for the ``_fk.mp4``
     render) — world-space, Y-up, grounded so the T-pose's lowest point sits
     at Y=0, uniformly scaled to ``target_diameter`` across every object type
     (see ``data_process/utils/skeleton.py::align_root_to_ground`` and
     ``extract_features.py``). That shared scale is what makes one absolute
     threshold meaningful across wildly different skeletons (a spider and a
     bear share the same canonical diameter).
  3. Identify the skeleton's ground-contact end effectors generically: the
     kinematic leaves (no children) whose T-pose height sits near the
     skeleton's lowest point. This is topology-based rather than name-based
     on purpose — UniMate trains on bipedal/quadrupedal/insectoid/avian/
     serpentine/marine rigs from three heterogeneous sources, and most
     Objaverse rigs never resolve to clean anatomical names (see
     ``data_process/joint_annotation/vocab.py``), so a "find the joint named
     Foot" rule would silently skip most of the dataset.
  4. Per contact joint, per frame: vertical distance to the ground plane
     (penetration when negative) and horizontal (XZ) displacement between
     consecutive frames where the joint is classified "in contact" (foot
     slide / skating).
  5. Aggregate to one row per clip and flag clips whose worst joint exceeds
     the slide-rate or penetration-depth threshold.

Usage (from the repo root)::

    python -m unimate.tools.eval_foot_contact <exp_dir>/samples \\
        --cond_glob "dataset/features/*/cond.npy"

Caveat: body types with no discrete limbs (serpentine, marine) have no
T-pose leaf that is semantically a "foot" — the geometric rule still picks
the single closest-to-ground leaf as a fallback (``contact_fallback=True``
in the report) so every clip gets a signal, but a flag on those rows means
"something touches/slides along the ground," not "a foot skates." Triage
those separately rather than tuning the global thresholds around them.
"""

import argparse
import csv
import glob
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np

from unimate.utils.logger import get_logger
from unimate.utils.motion_utils import recover_unimate_joint_pos_from_rot

logger = get_logger(file_name=__file__)

DEFAULT_COND_GLOB = 'dataset/features/*/cond.npy'
FPS = 30  # matches unimate.utils.visualization.FPS — no fps is saved with the .npy

# All in canonical units: every object type is scaled to the same
# --target_diameter (default 2.0) during feature extraction, so one absolute
# threshold is comparable across skeletons.
DEFAULT_CONTACT_HEIGHT = 0.06      # foot counted as "on the ground" below this height
DEFAULT_PENETRATION_EPS = 0.01     # ignore penetration noise below this depth
DEFAULT_GROUND_BAND = 0.15         # T-pose leaves within this of the lowest point are feet
DEFAULT_SLIDE_FLAG_PER_SEC = 0.75  # cumulative contact-frame slide, worst joint, per second
DEFAULT_PENETRATION_FLAG = 0.08    # worst single-frame penetration depth


# ---------------------------------------------------------------------------
# Skeleton lookup
# ---------------------------------------------------------------------------

def resolve_object_type(npy_path: str) -> str:
    """Filenames are ``{object_type}-...`` for every case saved by
    ``visualize_and_save_motions`` (``case_id``/``npy_lead`` both start with
    the object type)."""
    return os.path.basename(npy_path).split('-')[0]


def load_cond_dicts(cond_glob: str) -> Dict[str, dict]:
    """Merge every ``cond.npy`` matched by *cond_glob* into one
    ``{object_type: entry}`` map."""
    paths = sorted(glob.glob(cond_glob))
    if not paths:
        raise SystemExit(f"No cond.npy matched by {cond_glob!r}")
    merged: Dict[str, dict] = {}
    for path in paths:
        cond = np.load(path, allow_pickle=True).item()
        for object_type, entry in cond.items():
            if object_type in merged:
                logger.warning(
                    f"object_type {object_type!r} already loaded from another "
                    f"cond file; ignoring the copy in {path!r}."
                )
                continue
            merged[object_type] = entry
    return merged


# ---------------------------------------------------------------------------
# Ground-contact joint selection
# ---------------------------------------------------------------------------

@dataclass
class ContactJoints:
    indices: List[int]
    labels: List[str]
    fallback: bool  # True when no leaf was actually near the ground


def find_ground_contact_joints(
    cond_entry: dict, ground_band: float = DEFAULT_GROUND_BAND,
) -> ContactJoints:
    """Pick the skeleton's ground-contact end effectors from its T-pose.

    A ground-contact joint is a kinematic leaf (no children) whose T-pose
    height is within *ground_band* of the skeleton's lowest point — this
    covers feet/toes/hooves/paws/claws for any topology without depending on
    joint-name vocabulary. When nothing qualifies (a body plan with no
    discrete limbs near the ground), fall back to the single lowest leaf so
    every clip still gets a signal.
    """
    parents = np.asarray(cond_entry['parents']).ravel()
    n = len(parents)
    has_child = np.zeros(n, dtype=bool)
    for p in parents:
        if 0 <= p < n:
            has_child[p] = True
    leaves = np.where(~has_child)[0]
    if leaves.size == 0:  # degenerate single-joint skeleton
        leaves = np.array([0])

    tpos = np.asarray(cond_entry['tpos_first_frame'])[:, :3]
    # The lowest point of the whole T-pose, not just the leaves: a body part
    # that is not a kinematic leaf (a snake's belly, say) can sit lower than
    # every leaf, in which case no leaf qualifies and the fallback below is
    # what actually fires.
    ground_y = float(tpos[:, 1].min())
    leaf_heights = tpos[leaves, 1]

    near_ground = leaves[leaf_heights <= ground_y + ground_band]
    fallback = near_ground.size == 0
    if fallback:
        near_ground = np.array([leaves[int(np.argmin(leaf_heights))]])

    names = cond_entry.get('clean_joint_names')
    if names is None:
        names = cond_entry.get('joint_names')
    labels = [
        str(names[i]) if names is not None and i < len(names) else str(i)
        for i in near_ground
    ]
    return ContactJoints(indices=near_ground.tolist(), labels=labels, fallback=fallback)


# ---------------------------------------------------------------------------
# Per-clip metric
# ---------------------------------------------------------------------------

def evaluate_clip(
    global_positions: np.ndarray,
    contact_joints: ContactJoints,
    fps: float,
    contact_height: float,
    penetration_eps: float,
    slide_flag_per_sec: float,
    penetration_flag: float,
) -> Optional[dict]:
    """``global_positions``: ``(T, J, 3)`` world Y-up, grounded canonical frame."""
    T = global_positions.shape[0]
    if T < 2 or not contact_joints.indices:
        return None

    joint_pos = global_positions[:, contact_joints.indices, :]  # (T, K, 3)
    heights = joint_pos[:, :, 1]                                 # (T, K)
    xz = joint_pos[:, :, [0, 2]]                                 # (T, K, 2)

    max_penetration = float(np.clip(-heights, 0.0, None).max())
    penetration_frame_frac = float((heights < -penetration_eps).any(axis=1).mean())

    contact = heights <= contact_height                          # (T, K)
    step = np.linalg.norm(xz[1:] - xz[:-1], axis=-1)              # (T-1, K)
    both_in_contact = contact[1:] & contact[:-1]
    slide = np.where(both_in_contact, step, 0.0)

    duration_s = T / fps
    total_slide = float(slide.sum(axis=0).max())  # worst single joint over the clip
    slide_per_sec = total_slide / duration_s
    max_frame_slide = float(slide.max()) if slide.size else 0.0
    contact_frame_frac = float(contact.any(axis=1).mean())

    flagged = slide_per_sec > slide_flag_per_sec or max_penetration > penetration_flag

    return dict(
        n_frames=T,
        max_penetration=max_penetration,
        penetration_frame_frac=penetration_frame_frac,
        total_slide=total_slide,
        slide_per_sec=slide_per_sec,
        max_frame_slide=max_frame_slide,
        contact_frame_frac=contact_frame_frac,
        flagged=flagged,
    )


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------

FIELDNAMES = [
    'clip', 'object_type', 'contact_joints', 'contact_fallback', 'n_frames',
    'max_penetration', 'penetration_frame_frac', 'total_slide', 'slide_per_sec',
    'max_frame_slide', 'contact_frame_frac', 'flagged',
]


def sweep(
    samples_dir: str,
    cond_glob: str = DEFAULT_COND_GLOB,
    output_csv: Optional[str] = None,
    fps: float = FPS,
    contact_height: float = DEFAULT_CONTACT_HEIGHT,
    penetration_eps: float = DEFAULT_PENETRATION_EPS,
    ground_band: float = DEFAULT_GROUND_BAND,
    slide_flag_per_sec: float = DEFAULT_SLIDE_FLAG_PER_SEC,
    penetration_flag: float = DEFAULT_PENETRATION_FLAG,
) -> List[dict]:
    motions_dir = os.path.join(samples_dir, 'motions')
    npy_paths = sorted(glob.glob(os.path.join(motions_dir, '*.npy')))
    if not npy_paths:
        raise SystemExit(f"No .npy motion files under {motions_dir!r}")

    cond_dicts = load_cond_dicts(cond_glob)
    contact_cache: Dict[str, ContactJoints] = {}

    rows: List[dict] = []
    skipped: List[Tuple[str, str]] = []

    for path in npy_paths:
        clip_name = os.path.splitext(os.path.basename(path))[0]
        object_type = resolve_object_type(path)
        cond_entry = cond_dicts.get(object_type)
        if cond_entry is None:
            skipped.append((clip_name, f"object_type {object_type!r} not in cond_glob"))
            continue

        if object_type not in contact_cache:
            contact_cache[object_type] = find_ground_contact_joints(cond_entry, ground_band)
        contact_joints = contact_cache[object_type]

        parents = np.asarray(cond_entry['parents']).ravel()
        offsets = np.asarray(cond_entry['offsets'])
        motion = np.load(path)
        if motion.ndim != 3 or motion.shape[1] != len(parents):
            skipped.append((
                clip_name,
                f"joint-count mismatch: motion={motion.shape} cond_joints={len(parents)}",
            ))
            continue

        global_positions = recover_unimate_joint_pos_from_rot(motion, parents, offsets)
        metrics = evaluate_clip(
            global_positions, contact_joints, fps, contact_height,
            penetration_eps, slide_flag_per_sec, penetration_flag,
        )
        if metrics is None:
            skipped.append((clip_name, "clip too short or no contact joints resolved"))
            continue

        rows.append(dict(
            clip=clip_name,
            object_type=object_type,
            contact_joints=','.join(contact_joints.labels),
            contact_fallback=contact_joints.fallback,
            **metrics,
        ))

    rows.sort(key=lambda r: (not r['flagged'], -r['slide_per_sec'], -r['max_penetration']))

    output_csv = output_csv or os.path.join(samples_dir, 'foot_contact_report.csv')
    out_dir = os.path.dirname(output_csv)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    n_flagged = sum(r['flagged'] for r in rows)
    logger.info(
        f"Evaluated {len(rows)} clips ({len(skipped)} skipped) from {motions_dir!r}; "
        f"{n_flagged} flagged (slide > {slide_flag_per_sec} units/s or "
        f"penetration > {penetration_flag} units). Report: {output_csv}"
    )
    for clip_name, reason in skipped[:20]:
        logger.warning(f"Skipped {clip_name}: {reason}")
    if len(skipped) > 20:
        logger.warning(f"... and {len(skipped) - 20} more skipped clips.")

    return rows


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def parse_args():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('samples_dir', help="Output dir from unimate.inference.sample "
                                        "(contains a 'motions/' subdir of .npy files).")
    ap.add_argument('--cond_glob', default=DEFAULT_COND_GLOB,
                    help=f"Glob for cond.npy files to resolve skeletons from "
                         f"(default: {DEFAULT_COND_GLOB!r}).")
    ap.add_argument('--output_csv', default=None,
                    help="Report path (default: <samples_dir>/foot_contact_report.csv).")
    ap.add_argument('--fps', type=float, default=FPS)
    ap.add_argument('--contact_height', type=float, default=DEFAULT_CONTACT_HEIGHT,
                    help="Canonical-unit height below which a joint counts as grounded.")
    ap.add_argument('--penetration_eps', type=float, default=DEFAULT_PENETRATION_EPS,
                    help="Canonical-unit depth below which penetration is treated as noise.")
    ap.add_argument('--ground_band', type=float, default=DEFAULT_GROUND_BAND,
                    help="Canonical-unit band used to pick T-pose leaves as feet.")
    ap.add_argument('--slide_flag_per_sec', type=float, default=DEFAULT_SLIDE_FLAG_PER_SEC,
                    help="Flag a clip when its worst joint's cumulative contact-frame "
                         "slide exceeds this many canonical units per second.")
    ap.add_argument('--penetration_flag', type=float, default=DEFAULT_PENETRATION_FLAG,
                    help="Flag a clip when its worst single-frame penetration depth "
                         "exceeds this many canonical units.")
    return ap.parse_args()


def main():
    args = parse_args()
    rows = sweep(
        samples_dir=args.samples_dir,
        cond_glob=args.cond_glob,
        output_csv=args.output_csv,
        fps=args.fps,
        contact_height=args.contact_height,
        penetration_eps=args.penetration_eps,
        ground_band=args.ground_band,
        slide_flag_per_sec=args.slide_flag_per_sec,
        penetration_flag=args.penetration_flag,
    )
    flagged = [r for r in rows if r['flagged']]
    if flagged:
        logger.info("Worst offenders:")
        for r in flagged[:10]:
            logger.info(
                f"  {r['clip']} [{r['object_type']}]: "
                f"slide={r['slide_per_sec']:.3f} units/s, "
                f"penetration={r['max_penetration']:.3f} units"
                + (" (contact_fallback)" if r['contact_fallback'] else "")
            )


if __name__ == '__main__':
    main()
