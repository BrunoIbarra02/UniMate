# horse_nopost catalogue-verb feasibility test — 2026-11-02

## Scope and hypothesis

Authoritative catalogue entry: `idle, walk, trot, canter, gallop, rear, buck,
jump, graze, drink, neigh, paw ground, shake mane, lie down/get up, kick, pull
carriage`.

This single-species test generated exactly one new repetition of `trot`,
`canter`, `gallop`, `buck`, and `rear`. The earlier generic `run` and `jump`
clips were not regenerated or altered. No other species was started.

The test records generation and instrumental QA only. Whether the catalogue
verbs improve prompt match is reserved for Claude's visual review; nothing in
this report is `technical_validated` or `approved`.

Output root:
`/home/ubuntu/skintokens_quad10_20261027/anim_wave_20261102/`.

## Exact prompts

| Action | Exact prompt |
|---|---|
| trot | `A horse trots forward.` |
| canter | `A horse canters forward.` |
| gallop | `A horse gallops forward at full speed.` |
| buck | `A horse bucks, kicking its hind legs high.` |
| rear | `A horse rears up onto its hind legs.` |

The exact manifests are preserved in the wave root as
`cases_horse_catalogue_canary.json` and
`cases_horse_catalogue_remainder.json`.

## Generation and QA accounting

All five clips use `horse_nopost`, CFG 3.0, seed 0, one repetition, one
60-frame latent segment, and no `--motion_expand`. The runner uses
`scripts/run_sample_motion_text.sh`, exports only the explicitly requested NPY
files, and reuses the wave's Blender audit, 24 fps preview, contact frames,
contact sheet, glTF Hips-curve extraction, and ffprobe pipeline.

Physical counts for the five new clips: 5 NPY, 5 GLB, 5 FBX, 5 audit JSON,
5 MP4, 40 contact PNG, 5 sheets, 5 curve JSON, and 5 probe JSON. Every preview
probe reports 24 fps, 49 frames, and 2.041667 s. Every Hips curve contains 60
samples over 1.966667 s. The consolidated
`raw_metrics_summary.{json,tsv}` now contains 33 rows (20 original run/jump,
8 deer catalogue clips, and these 5 horse clips).

The runner passed `bash -n` and `tools/preflight_batch_check.sh`. `trot` was
executed first as a complete canary; only after its `QA_DONE` marker were the
other four sampled. All five finished with `QA_DONE`, and no runner or sampler
remained active afterward.

## Raw instrumental numbers

These values are evidence only, not quality gates or visual verdicts.

| action | audit frames | edge p99 / max | floor min / max | moving legs | seam | Hips range X / Y / Z | Hips path | speed mean / max | accel max | Y peaks > start+0.08 | probe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| trot | 48 | 2.314283 / 21.636520 | -0.069415 / 0.020266 | 16/16 | 0.059842 | 0.103269 / 3.069426 / 0.031560 | 3.075641 | 1.563885 / 1.720170 | 1.923977 | 0 | 24 fps; 49 frames; 2.041667 s |
| canter | 48 | 1.056261 / 1.363659 | -0.011145 / 0.000000 | 5/16 | 0.008288 | 0.011981 / 0.007221 / 0.026106 | 0.135057 | 0.068673 / 0.229801 | 5.900492 | 0 | 24 fps; 49 frames; 2.041667 s |
| gallop | 48 | 1.944579 / 12.186424 | -0.050804 / 0.013627 | 16/16 | 0.048724 | 0.016202 / 0.046593 / 0.050594 | 0.199876 | 0.101632 / 0.288449 | 7.443924 | 0 | 24 fps; 49 frames; 2.041667 s |
| buck | 48 | 2.030857 / 23.060067 | -0.092911 / 0.000000 | 16/16 | 0.047440 | 0.018508 / 0.119343 / 0.098403 | 0.360296 | 0.183201 / 0.557872 | 5.228959 | 1 | 24 fps; 49 frames; 2.041667 s |
| rear | 48 | 1.648797 / 7.644574 | -0.005102 / 0.094474 | 15/16 | 0.045757 | 0.007469 / 0.017969 / 0.143091 | 0.186223 | 0.094690 / 0.279601 | 6.774534 | 0 | 24 fps; 49 frames; 2.041667 s |

SkinTokens/Hugging Face, `backend/app.py`, S3, ECS, and deployment were not
touched.
