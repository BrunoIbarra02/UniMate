# Offline cranial-accessory annotation investigation — 2026-11-02

## Scope and safety boundary

This investigation reused the ten existing GLBs under
`/home/ubuntu/skintokens_quad10_20261027/rig_wave_20261101/rigs/`.
It made no SkinTokens or Hugging Face Space call and ran no new GPU inference.
Only the offline Blender topology labeler and the annotation validator were
rerun. `backend/app.py`, deployment state, and approval fields were untouched.

## Finding

The hoped-for category was only partly correct. Five variants contain a narrow,
repeatable structure that the old labeler did not recognize: two short linear
chains attached to `Head`, mirrored across the inferred anatomical right axis,
and rising above the head. Horse variants also contain one separate midline
chain extending forward below the ears, which is a muzzle.

Other variants are not safe instances of the same template:

- `bull_nopost`: 16 equal-length rays directly attached to `Head`, plus eight
  non-cranial generic bones. This is not a defensible ear/horn vocabulary gap.
- `bull_conservative`: six non-mirrored terminal head rays. The horn/ear/muzzle
  identity is ambiguous from topology and rest geometry.
- `giraffe_conservative`: duplicated coincident branches (`bone_20` and
  `bone_21` have identical geometry), and eight additional generic bones away
  from the cranial subtree.
- `elk_nopost`: several real-looking paired antler/ear chains coexist with
  three unmatched short branches and two non-cranial generic bones. Blanket
  classification would hide uncertainty.
- `yak_conservative`: still fails before annotation with
  `no hierarchical rear/front load-bearing fork pair found`.

## Targeted implementation

Remote script:
`/home/ubuntu/skintokens_quad10_20261027/rig_wave_20261101/tools/auto_label_unirig_quadruped_v2.py`

- Original SHA-256: `bf1503564e29c41abc303c509be4d68df316aa2a0d906bd9fa5578dc7099a738`
- Patched SHA-256: `1c07c5a10305a2126cb845a670f4f63e3f03b21429869d2d54e481957689d1cf`
- Recoverable backup:
  `auto_label_unirig_quadruped_v2.py.pre_cranial_template_20261102.bak`

The new detector accepts only:

1. exactly two simple chains that have equal topology, comparable segment
   lengths, opposite lateral signs, mirrored right/forward/up coordinates, and
   elevated tips; or
2. that same unique ear pair plus exactly one linear midline chain extending
   forward below the ear tips, labelled `Muzzle`.

Every other cranial branch remains `Bone` with
`unmapped_cranial_accessory`, so the validator continues to fail closed. The
existing reviewed terminal-fan template remains as a fallback. The anatomy
report now records which `cranial_template` was used.

## Final rerun on the same ten GLBs

| Variant | Auto-label | `validate --reviewed` | Result |
|---|---:|---:|---|
| `horse_nopost` | 0 | 0 | PASS; 5 Muzzle + 6 Ear joints |
| `horse_conservative` | 0 | 0 | PASS; 1 Muzzle + 6 Ear joints |
| `bull_nopost` | 0 | 2 | FAIL closed |
| `bull_conservative` | 0 | 2 | FAIL closed |
| `zebra_nopost` | 0 | 0 | PASS; 2 Ear joints |
| `zebra_conservative` | 0 | 0 | PASS; 6 Ear joints |
| `donkey_conservative` | 0 | 0 | PASS; 4 Ear joints |
| `giraffe_conservative` | 0 | 2 | FAIL closed |
| `elk_nopost` | 0 | 2 | FAIL closed |
| `yak_conservative` | 1 | not run | structural FAIL before annotation |

Total: **5/10 pass**. Evidence is under
`rig_wave_20261101/cranial_vocab_eval_20261102/final_deployed/`.

Five prior automatic positives were also compared before/after the patch:
`sheep_nopost`, `wolf_nopost`, `wolf_conservative`,
`raccoon_conservative`, and `deer_nopost`. All remained 5/5 accepted.

## Reuse decision

The bilateral simple-ear template is safe to reuse automatically when all its
geometric and topological predicates pass; otherwise it does nothing. Horn,
antler, ossicone, and mane classification is **not** generalized by this change.
Those features still require a separately validated narrow template and human
sign-off per species/rig until enough clean examples exist.

These are rig-annotation results only. No variant is approved,
`technical_validated`, action-generated, or visually accepted for animation by
this work.
