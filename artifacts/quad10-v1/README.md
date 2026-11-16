# Quad10 rig release v1

`traceability_matrix.json` and `TRACEABILITY_MATRIX.md` provide the verified 28-asset
traceability baseline connecting species, catalog/taxonomic family, rig version/hash,
two cycle repetitions, remote/local asset paths, packed 4K diffuse textures, and
anchored visual verdicts from Claude Code.

`qa_report.json` is the deterministic release gate for the ten selected
profiles. It combines fresh annotation/canonical-facing validation, two Blender
mesh-motion audits per profile, and content hashes for the canonical GLBs.

Nine passing rigs were frozen under content-addressed S3 keys. Cow remains
blocked: its conservative rig has a metric-confirmed tear and its nopost rig has
coincident hind-limb branches, so neither is safe to publish without a new rig
or a manual skin-weight repair followed by full visual QA.

`publication.json` records the criterion-6 proof: `run` was generated from the
already frozen goat rig, audited, visually sampled, and published with
`human_review_required` metadata. No SkinTokens re-rigging was performed.

Reproduce the local gate from the existing audit bundle:

```powershell
python scripts/qa_quad10_release.py `
  --plan artifacts/quad10-v1/release_plan.json `
  --metadata artifacts/quad10-v1/source_metadata.json `
  --audit-dir tmp/skintokens_quad10_20261027/audits `
  --output artifacts/quad10-v1/qa_report.json
```
