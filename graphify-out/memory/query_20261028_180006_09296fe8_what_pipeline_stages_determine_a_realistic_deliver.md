---
type: "query"
date: "2026-10-28T18:00:06.126721+00:00"
question: "What pipeline stages determine a realistic delivery date for each animal family?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["preprocess_asset()", "canonicalize_anim()", "align_initial_facing()", "animate_lbs()"]
---

# Q: What pipeline stages determine a realistic delivery date for each animal family?

## Answer

Expanded from graph vocab: animal, family, rig, skeleton, skinning, preprocess, label, motion, animation, dataset. The production plan must treat preprocessing, canonical skeleton alignment, facing, LBS export, and motion QA as separate gates. A file existing is not proof of family readiness.

## Outcome

- Signal: useful

## Source Nodes

- preprocess_asset()
- canonicalize_anim()
- align_initial_facing()
- animate_lbs()