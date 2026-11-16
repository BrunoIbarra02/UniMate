# baboon_nopost full-action feasibility test — 2026-11-04

## Scope and accounting

Authoritative catalogue entry: `idle, walk, run, climb, sit, forage, groom,
vocalize, threaten, bite, carry infant`.

- Newly generated and instrumentally QA'd: 8/8 requested clips (`idle`, `run`,
  `sit`, `forage`, `groom`, `vocalize`, `threaten`, `bite`).
- Reused without regeneration: `walk`, referenced from the wave5 gate at
  `/home/ubuntu/skintokens_local/rig_wave5_local_20261103/walk_test/baboon_nopost/`.
  The wave folder contains symlinks under `baboon/walk_reused/`. Source SHA-256:
  GLB `74e0445fe04433dc4364a03e9365466f5a372198a45fb06d565cd52f09dcd85b`;
  MP4 `37dd916bb91ee2b90053bdbef64805431993d4e9381cf492c50872b9b1193e67`.
- baboon: climb — excluded because it is structurally impossible in the current
  single-animal pipeline without an external support surface; no substitute was attempted.
- baboon: carry infant — excluded because it requires a second body; no substitute
  was attempted.
- Extra visual scrutiny required: `vocalize`, because a text-to-motion result may
  be visually indistinguishable from idle.
- Visual verdict: pending Claude review. Nothing is `technical_validated` or `approved`.

Output root:
`/home/ubuntu/skintokens_quad10_20261027/anim_wave5_species_20261104/baboon/`.

## Exact prompts

| Action | Exact prompt |
|---|---|
| idle | `A baboon remains still in a relaxed idle pose, breathing gently.` |
| run | `A baboon runs forward.` |
| sit | `A baboon sits down and remains seated.` |
| forage | `A baboon searches the ground for food with its hands.` |
| groom | `A baboon grooms its fur with its hands.` |
| vocalize | `A baboon opens its mouth and vocalizes loudly.` |
| threaten | `A baboon makes a threatening display, baring its teeth and raising its body.` |
| bite | `A baboon lunges forward and bites.` |

The exact prompts are also preserved in
`cases_baboon_catalogue_{canary,remainder}.json` and `catalogue_scope.json`.

## Generation and QA facts

All new clips use `baboon_nopost`, CFG 3.0, seed 0, one repetition, one
60-frame latent segment and no `--motion_expand`. The runner is a narrow
derivative of the validated deer catalogue runner and uses
`scripts/run_sample_motion_text.sh`, `run_animate_motion.sh`, the existing
Blender animation audit, 24 fps preview rendering, eight-frame contact
rendering and sheet assembly, direct glTF curve analysis, and ffprobe.

The runner passed `bash -n` and `tools/preflight_batch_check.sh`. The canary
`idle` completed with all QA before the remaining seven actions were released.
Input annotation revalidation passed with `accepted=true`, human-reviewed,
40 joints, zero generic bones and no issues. No structural or export error
occurred.

Physical counts for the eight new clips: 8 NPY, 8 GLB, 8 FBX, 8 animation
audit JSON, 8 MP4, 64 contact PNG, 8 sheets, 8 curve JSON and 8 probe JSON.
Every audit covers 48 frames. Every preview probe reports 24 fps, 49 frames
and 2.041667 s. Every Hips curve contains 60 samples over 1.966667 s.

Raw numbers below are evidence only, not quality gates or prompt-match verdicts.

| action | edge p99 / max | moving legs | seam | Hips range Y / Z |
|---|---:|---:|---:|---:|
| idle | 1.365124 / 2.938941 | 14/16 | 0.021351 | 0.031267 / 0.035264 |
| run | 2.629331 / 15.688820 | 16/16 | 0.028849 | 0.042965 / 0.035315 |
| sit | 1.840277 / 8.909050 | 16/16 | 0.132744 | 0.137190 / 0.249201 |
| forage | 1.946016 / 9.799690 | 13/16 | 0.064671 | 0.020788 / 0.067840 |
| groom | 1.408636 / 4.774889 | 6/16 | 0.043698 | 0.023240 / 0.008362 |
| vocalize | 1.511302 / 10.347583 | 7/16 | 0.041220 | 0.013107 / 0.019396 |
| threaten | 1.764943 / 8.888572 | 16/16 | 0.077091 | 0.089567 / 0.089392 |
| bite | 2.322952 / 12.934564 | 16/16 | 0.067411 | 0.891086 / 0.193136 |

No other species was started. SkinTokens/HF Space, `backend/app.py`, S3, ECS
and deployment were untouched. GPU and QA runners were idle after completion.

