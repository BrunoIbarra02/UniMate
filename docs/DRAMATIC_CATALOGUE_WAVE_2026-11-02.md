# Dramatic catalogue wave — generation and instrumental QA

Date: 2026-11-02 (Asia/Riyadh)  
Remote output: `/home/ubuntu/skintokens_quad10_20261027/anim_wave_20261102/`

## Scope and status

Generated exactly one single-segment repetition for each of the 21 explicitly
requested dramatic actions across 14 already walk-confirmed rig variants. No
trot/canter-like variants or unrequested actions were added. Settings were CFG
3.0, seed 0, one repetition, 60 latent frames, without `--motion_expand`.

Physical result: 21/21 new NPY, 21/21 GLB, 21/21 FBX, 21/21 audit JSON,
21/21 preview MP4, 168 contact PNG, 21/21 contact sheets, 21/21 curve JSON,
and 21/21 ffprobe JSON. Each audit covered 48 frames; every curve contains 60
samples over 1.966667 s; every preview is 24 fps, 49 frames, 2.041667 s.

This report contains no visual-quality judgment. All 21 clips remain pending
Claude's visual review. Nothing is `technical_validated` or `approved`.

## Exact prompts

| Variant | Action id | Exact prompt |
|---|---|---|
| `dog_nopost` | `sprint` | `A dog sprints forward at full speed.` |
| `dog_nopost` | `jump` | `A dog jumps into the air.` |
| `buffalo_nopost` | `charge` | `A buffalo charges forward aggressively.` |
| `pig_conservative` | `charge` | `A pig charges forward aggressively.` |
| `bison_nopost` | `charge` | `A bison charges forward aggressively.` |
| `bear_nopost` | `climb` | `A bear climbs upward using all four limbs.` |
| `bear_nopost` | `swim` | `A bear swims forward through water.` |
| `goat_nopost` | `climb` | `A goat climbs upward over a steep surface.` |
| `goat_nopost` | `jump` | `A goat jumps into the air.` |
| `cougar_nopost` | `jump` | `A cougar jumps powerfully into the air.` |
| `cougar_nopost` | `pounce` | `A cougar crouches and pounces forward onto its target.` |
| `hippopotamus_nopost` | `bite_charge` | `An object charges and bites aggressively.` |
| `raccoon_conservative` | `climb` | `A raccoon climbs upward using all four limbs.` |
| `wolf_conservative` | `sprint` | `A wolf sprints forward at full speed.` |
| `zebra_nopost` | `gallop` | `A zebra gallops forward at full speed.` |
| `zebra_nopost` | `kick` | `A zebra kicks backward forcefully with its hind legs.` |
| `zebra_nopost` | `rear` | `A zebra rears up onto its hind legs.` |
| `wolverine_nopost` | `climb` | `A wolverine climbs upward using all four limbs.` |
| `otter_conservative` | `dive` | `An otter dives headfirst down into the water.` |
| `otter_conservative` | `roll` | `An otter rolls its entire body over sideways.` |
| `donkey_conservative` | `kick` | `A donkey kicks backward forcefully with its hind legs.` |

## Execution discipline and incidents

The new runner passed `bash -n` and
`tools/preflight_batch_check.sh` before the first launch. Dog was run alone as
the canary and the other 19 clips were not released until dog had a complete
2/2 QA bundle.

The first dog invocation caught one plumbing bug before inference: the legacy
dog/bear layout ends in `dog_nopost/asset/`, and the runner initially treated
the leaf name `asset` as the variant. It exited with `MISSING_INPUT` before
sampling. The variant resolver was corrected, then `bash -n` and preflight
were repeated successfully. No motion was regenerated or lost in that failed
attempt.

All 14 exact assets and annotations resolved across the original dog/bear
sweep, original quad10, `rig_wave_20261101`, and `rig_wave2_20261101`. Every
pre-sampling annotation validation returned `accepted=true`, human-reviewed,
and `issues=[]`.

No rig audit process errored. The raw audit range includes an
`edge_stretch_max` outlier of 135.160833 for
`wolf_conservative-sprint-rep_0-11`; this is reported as a raw instrumental
outlier, not forced into a structural-failure or visual-quality verdict. Claude
must inspect the MP4 and contact sheet separately.

## Raw evidence

- Full consolidated folder summary (54 rows including the 33 earlier clips):
  `anim_wave_20261102/raw_metrics_summary.{json,tsv}`.
- Local captured copies:
  `tmp/dramatic_catalogue_wave_20261102/raw_metrics_summary.{json,tsv}`.
- Exact manifests and runner:
  `tmp/dramatic_catalogue_wave_20261102/`.
- Remote QA subfolders: `audits/`, `previews/`, `frames/`, `sheets/`,
  `curves/`, and `probes/` under the remote output root above.

Cross-checking the two manifests against the consolidated summary selected
exactly 21 unique expected rows with zero missing rows. Across those rows:

- `edge_stretch_p99_max`: 1.156911–4.695200;
- `edge_stretch_max`: 4.625171–135.160833;
- `moving_leg_bone_count_5deg`: 3–16;
- ffprobe values: uniformly `24/1`, 49 frames, 2.041667 s.

No SkinTokens/Hugging Face call, S3 copy, `backend/app.py` edit, deployment, or
publication was performed.
