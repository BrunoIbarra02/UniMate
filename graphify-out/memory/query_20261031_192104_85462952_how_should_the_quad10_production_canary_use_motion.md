---
type: "query"
date: "2026-10-31T19:21:04.450232+00:00"
question: "How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["sample.py", "motion_expansion.py", "build_overlap_keep_mask()", "_load_test_cases_json()"]
---

# Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?

## Answer

Expanded from graph vocabulary: motion, expand, sample, annotation, blender, rig, quality, overlap, test, cases, animation, validate. The graph located sample.py and motion_expansion.py: motion_expand consumes prompt lists, validates overlap against config.dataset.max_motion_length, chains segments with build_overlap_keep_mask/expand_motion_chain, and saves per-repetition motions. The production run verified max_motion_length=60, used two segments with overlap 10 for 110 latent frames, then applied existing annotation, Blender audit, and rig-quality symmetry tooling to frozen rigs.

## Outcome

- Signal: useful

## Source Nodes

- sample.py
- motion_expansion.py
- build_overlap_keep_mask()
- _load_test_cases_json()