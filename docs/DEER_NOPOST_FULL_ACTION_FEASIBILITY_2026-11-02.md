# deer_nopost full-action feasibility test — 2026-11-02

## Scope and accounting

Authoritative catalogue entry: `idle, walk, trot, run, bound, graze, browse,
drink, alert, call, antler clash, lie down`.

- Newly generated and instrumentally QA'd: 8/8 requested clips (`trot`,
  `bound`, `graze`, `browse`, `drink`, `alert`, `call`, `lie down`).
- Pre-existing and visually confirmed today: `walk`, `run`; neither motion was
  resampled.
- Excluded: `antler clash` — multi-character interaction, needs separate
  handling. No single-animal substitute was attempted.
- `idle` was not included in Bruno's enumerated eight new generations and was
  not generated in this test.
- Visual verdict: pending Claude review. Nothing is `technical_validated` or
  `approved`.

Output root:
`/home/ubuntu/skintokens_quad10_20261027/anim_wave_20261102/`.

## Exact prompts

| Action | Exact prompt |
|---|---|
| trot | `An object trots.` |
| bound | `An object bounds forward.` |
| graze | `An object grazes, lowering its head to eat grass.` |
| browse | `An object browses, reaching its head toward foliage.` |
| drink | `An object drinks, lowering its head to water.` |
| alert | `An object stands alert, head raised.` |
| call | `An object calls out.` |
| lie down | `An object lies down.` |

Prompt manifests are preserved as `cases_deer_catalogue_canary.json` and
`cases_deer_catalogue_remainder.json` in the output root.

## Generation and QA facts

All clips use `deer_nopost`, CFG 3.0, seed 0, one repetition, one 60-frame
latent segment, and no `--motion_expand`. The runner is a direct derivative of
`anim_wave_20261102_runner.sh` and reuses `scripts/run_sample_motion_text.sh`
plus the same Blender audit, 24 fps preview, eight-frame contact sheet, glTF
curve, and ffprobe sequence.

Physical counts for the eight new clips: 8 NPY, 8 GLB, 8 FBX, 8 audit JSON,
8 MP4, 64 contact PNG, 8 sheets, 8 curve JSON, and 8 probe JSON. Every preview
probe reports 24 fps, 49 frames, and 2.041667 s; every Hips curve has 60 samples
and 1.966667 s.

Raw numbers below are evidence only, not quality gates or prompt-match verdicts.

| action | edge p99/max | moving legs | seam | Hips range Y/Z | Hips path |
|---|---:|---:|---:|---:|---:|
| trot | 1.232297 / 1.620644 | 0/16 | 0.038860 | 0.012813 / 0.013895 | 0.169176 |
| bound | 1.737678 / 4.803846 | 10/16 | 0.128716 | 0.100135 / 0.129265 | 0.274529 |
| graze | 1.303938 / 2.596908 | 7/16 | 0.039925 | 0.039281 / 0.016963 | 0.181146 |
| browse | 1.177990 / 1.507362 | 0/16 | 0.039578 | 0.037237 / 0.008719 | 0.093839 |
| drink | 1.833071 / 6.102864 | 8/16 | 0.179427 | 0.017915 / 0.009870 | 0.094735 |
| alert | 1.042264 / 1.166137 | 0/16 | 0.007708 | 0.005140 / 0.008113 | 0.074949 |
| call | 1.258463 / 2.203976 | 2/16 | 0.044107 | 0.005009 / 0.012049 | 0.095770 |
| lie down | 2.004915 / 5.908796 | 12/16 | 0.108791 | 0.187509 / 0.278515 | 0.383602 |

The consolidated `raw_metrics_summary.json` and `.tsv` in the wave root now
contain 28 rows: the prior 20 run/jump clips plus these eight.

## Orchestration incident and recovery

The first canary attempt exposed an accumulated-manifest bug in the derived
runner: the animation export step re-exported the 20 pre-existing GLB/FBX pairs
before exporting `trot`, then stopped before new QA on an unbound local `base`
variable. It did not resample the 20 motions and did not replace their QA
artifacts, but their GLB/FBX files were re-exported from the original motions.

The runner was changed to pass only the explicitly requested NPY files to
`run_animate_motion.sh`, and to initialize the QA asset root. It passed
`bash -n` and `preflight_batch_check.sh` again. `trot` resumed from its existing
motion without a second inference and completed all QA; only then were the
other seven actions launched. The final eight audits and all downstream QA
steps exited successfully. No other species was started.

SkinTokens/HF Space, `backend/app.py`, S3, ECS, and deployment were untouched.

