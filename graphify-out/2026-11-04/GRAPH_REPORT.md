# Graph Report - UniMate  (2026-11-04)

## Corpus Check
- 481 files · ~329,180 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 273 file(s) not represented in the graph (top: .log 256, .fbx 8, .tsv 7)

## Summary
- 2733 nodes · 5720 edges · 185 communities (96 shown, 89 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 122 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `021b8ceb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- preprocess_char.py
- blender_export.py
- numpy
- motion_utils.py
- sample.py
- patch_annotations.py
- sys
- topology.py
- recompute_topology_arrays
- ICPlan
- Diffusion Planning Math
- auto_label_unirig_quadruped_v2.py
- T5Conditioner
- Denoiser Base Class
- names_correct_llm.py
- Multi-view Character Rendering
- LlamaRMSNorm
- Transformer Blocks
- Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx
- motion_features.py
- torch
- Text Embedding Precomputation
- normalize_scene
- re
- numpy
- plotting.py
- train_diffusion
- conditioning.py
- schema.py
- caption_rewrite_llm.py
- Skeleton Alignment Utilities
- LLM Client Interface
- Sampler
- blocks/common.py
- Blender Rigging Utilities
- render_objaverse.py
- json
- extract_features.py
- Denoiser Model Variants
- dist_plot.py
- names_clean_llm.py
- .__init__
- Generative Base Trainer
- T5 Text Conditioner
- _extract_into_tensor
- vis_tpose.py
- Character Animation Scripts
- Joint Distribution Visualization
- eval_foot_contact.py
- mean_median_guides
- render_action_multiview
- blender_render.py
- math
- trainer.py
- load_and_prep_asset
- GraphAttnBias
- visualization.py
- vis_joint_count.py
- Metadata I/O
- merge_extra_bone_weights
- camera_pose_on_sphere
- recover_unimate_joint_pos_from_rot
- auto_label_unirig_quadruped_v2.original.py
- apply_joint_addition_ellipsoid
- face_select_llm.py
- plot_dataset
- argparse
- BERT and CLIP Encoders
- loguru
- cougar_nopost
- _build_spectral_encoder
- Matplotlib Ticker Formatting
- simplify_materials_for_fbx
- baboon_nopost full-action feasibility test — 2026-11-04
- Export Resume Markers
- metadata.py
- flatten_rgba
- goat_nopost
- Metadata Lookup Helpers
- hippopotamus_nopost
- wave5_supervisor.sh
- render_tpose.py
- InputLayer
- Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)
- BERTConditioner
- Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs
- MotionDataset
- wave5_validate_profiles.sh
- Cache Digest Utilities
- wave5_walk_one.sh
- GaussianDiffusion
- cougar_nopost-jump-rep_0-0.npy
- Agent Documentation
- FBX Animation Script
- LBS Animation Script
- Mixamo Animation Script
- NPZ Animation Script
- General Export Script
- LLM Face Correction
- Rule-based Face Selection
- Joint Name Cleaning
- LLM Joint Correction
- Facing Visualization Script
- T-Pose Visualization Script
- Character Preprocessing Script
- T-Pose Rendering Script
- cougar_nopost-jump-rep_1-0.npy
- Motion Expansion Script
- Motion In-betweening Script
- Text-to-Motion Script
- Model Training Script
- Dataset Loading Utilities
- Motion Editing Diagram
- Motion Expansion Diagram
- Motion In-betweening Diagram
- Qualitative Results Visualization
- Feature Extraction Module
- Data Processing Module
- Motion Rendering Module
- data_process/scripts/run_animate_motion.sh
- baboon_runner.sh
- os
- cougar_nopost-run-rep_0-0.npy
- bind_action
- Dramatic catalogue wave — generation and instrumental QA
- CLAUDE.md
- cougar_nopost-run-rep_1-0.npy
- agentops.md
- goat_nopost-jump-rep_0-0.npy
- goat_nopost-jump-rep_1-0.npy
- goat_nopost-run-rep_0-0.npy
- goat_nopost-run-rep_1-0.npy
- hippopotamus_nopost-jump-rep_0-0.npy
- hippopotamus_nopost-jump-rep_1-0.npy
- hippopotamus_nopost-run-rep_0-0.npy
- hippopotamus_nopost-run-rep_1-0.npy
- Canary run+jump ~4 s — 2026-10-31
- anim_wave_20261102_dramatic_runner.sh
- wave5_species_runner.sh
- samples
- run_canary_4s.sh
- continue_canary_4s.sh
- probe_results.sh
- rerender_24fps.sh
- Offline cranial-accessory annotation investigation — 2026-11-02
- horse_nopost catalogue-verb feasibility test — 2026-11-02
- Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?
- run_initial_wave.sh
- deer_nopost full-action feasibility test — 2026-11-02
- SpatioTemporalBlock
- run_rig_wave_profiles.sh
- run_offline_eval.sh
- run_hippo_wallow_fallback.sh
- prepare_rig_wave.sh
- run_walk_variants.sh
- 2026-11-02 21:55 +03:00 — dramatic catalogue wave started
- anim_wave_20261102_deer_catalogue_runner.sh
- anim_wave_20261102_horse_catalogue_runner.sh
- TimestepEmbedder

## God Nodes (most connected - your core abstractions)
1. `MotionDataset` - 38 edges
2. `GaussianDiffusion` - 37 edges
3. `MainConfig` - 30 edges
4. `2026-11-02 21:55 +03:00 — dramatic catalogue wave started` - 29 edges
5. `Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx` - 27 edges
6. `train_diffusion()` - 26 edges
7. `UniMateDenoiserBase` - 24 edges
8. `plot_dataset()` - 23 edges
9. `export_asset()` - 20 edges
10. `plot_comparison()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Data Process README` --references--> `UniML3D Teaser Diagram`  [EXTRACTED]
  data_process/README.md → assets/teaser.png
- `build_anim_from_npy()` --calls--> `recover_unimate_anim_from_rot()`  [EXTRACTED]
  data_process/mesh_animation/animate_motion.py → unimate/utils/motion_utils.py
- `build_anim_from_npy()` --calls--> `recover_unimate_joint_pos_from_ric()`  [EXTRACTED]
  data_process/mesh_animation/animate_motion.py → unimate/utils/motion_utils.py
- `visualize_and_save_motions()` --calls--> `render_skeleton_tpose()`  [EXTRACTED]
  unimate/utils/visualization.py → data_process/utils/plotting.py
- `visualize_and_save_motions()` --calls--> `render_skeleton_tpos_spectral()`  [EXTRACTED]
  unimate/utils/visualization.py → data_process/utils/plotting.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Data Processing Pipeline** — stage_1_export, stage_2_caption_category, stage_3_joint_annotation, stage_4_extract, stage_5_animate [EXTRACTED 1.00]
- **Animation Pipeline Stages** — graphify_out_memory_query_20261028_180006_09296fe8_what_pipeline_stages_determine_a_realistic_deliver_preprocess_asset, graphify_out_memory_query_20261028_180006_09296fe8_what_pipeline_stages_determine_a_realistic_deliver_canonicalize_anim, graphify_out_memory_query_20261028_180006_09296fe8_what_pipeline_stages_determine_a_realistic_deliver_align_initial_facing, graphify_out_memory_query_20261028_180006_09296fe8_what_pipeline_stages_determine_a_realistic_deliver_animate_lbs [EXTRACTED 1.00]
- **UniMate Core Execution Flow** — unimate_training_train, unimate_inference_sample, unimate_tools_precompute_text_emb [EXTRACTED 1.00]
- **UniML3D Data Processing Pipeline** — data_process_motion_export, data_process_motion_rendering, data_process_vlm_caption, data_process_joint_annotation, data_process_feature_extraction, data_process_mesh_animation [EXTRACTED 1.00]
- **Zero-Shot Motion Applications** — unimate_inference_sample, flow_matching [INFERRED 0.85]
- **Motion Generation and Editing Tasks** — assets_motion_editing, assets_motion_expansion, assets_motion_in_betweening [INFERRED 0.90]

## Communities (185 total, 89 thin omitted)

### Community 0 - "preprocess_char.py"
Cohesion: 0.04
Nodes (51): _action_bone_names(), _adopt_action(), animate_character_fbx(), parse_args(), animate_lbs(), extract_skin(), lbs_deform(), load_motion_local_mats() (+43 more)

### Community 1 - "blender_export.py"
Cohesion: 0.05
Nodes (34): cond_from_rest(), _apply_root_rotation(), build_rest_animation(), build_skeleton_arrays(), build_vertex_groups_sparse(), build_vgroup_to_bone_mapping(), children_from_parents(), choose_main_armature() (+26 more)

### Community 2 - "numpy"
Cohesion: 0.11
Nodes (11): apply_joint_addition_linear(), apply_joint_perturbation(), apply_joint_removal(), apply_skeleton_pooling(), bone_length_weighted_sample(), build_children_map(), collapse_single_child_joint(), delete_joint() (+3 more)

### Community 3 - "motion_utils.py"
Cohesion: 0.13
Nodes (7): _validate_motion(), compute_cont6d_params(), compute_local_velocity(), compute_rifke(), compute_rots_from_tpos(), compute_unimate_motion_feats(), recover_unimate_joint_pos_from_ric()

### Community 4 - "sample.py"
Cohesion: 0.06
Nodes (29): MainConfig, create_dataset(), build_joint_keep_mask(), get_joint_names(), parse_keep_joints(), parse_keep_frames(), _build_diffusion(), _encode_prompt() (+21 more)

### Community 5 - "patch_annotations.py"
Cohesion: 0.06
Nodes (33): apply_root_offsets(), load_json(), load_overrides(), load_rig_flags(), needs_side_from_x(), normalize_locomotion(), object_type_of(), patch_captions() (+25 more)

### Community 6 - "sys"
Cohesion: 0.08
Nodes (30): export_asset(), list_asset_files(), main(), parse_args(), pick_importer(), export_mixamo(), main(), export_objaverse() (+22 more)

### Community 7 - "topology.py"
Cohesion: 0.10
Nodes (14): build_topology_cond(), _adjacency_list(), _build_kinchains(), _build_laplacian(), _children_map(), compute_adjacency_matrix(), compute_edge_indexs(), compute_edge_relations_and_distances() (+6 more)

### Community 8 - "recompute_topology_arrays"
Cohesion: 0.20
Nodes (5): recompute_topology_arrays(), _adjacency_list(), _children_map(), compute_edge_relations_and_distances(), compute_joint_depths()

### Community 9 - "ICPlan"
Cohesion: 0.06
Nodes (5): expand_t_like_x(), GVPCPlan, ICPlan, VPCPlan, noise_ode()

### Community 10 - "Diffusion Planning Math"
Cohesion: 0.08
Nodes (21): add_qwen_model_args(), load_json(), load_qwen_model(), qwen_generate(), save_json(), _record(), aggregate_votes(), build_messages() (+13 more)

### Community 11 - "auto_label_unirig_quadruped_v2.py"
Cohesion: 0.11
Nodes (9): all_paths(), best_non_limb_path(), cranial_coordinates(), is_central_muzzle(), is_mirrored_ear_pair(), label_paw_branches(), lowest_path(), simple_chain() (+1 more)

### Community 12 - "T5Conditioner"
Cohesion: 0.09
Nodes (5): BaseConditioner, _hash_trick(), T5Conditioner, TorchAutocast, WhiteSpaceTokenizer

### Community 13 - "Denoiser Base Class"
Cohesion: 0.07
Nodes (30): UniML3D Teaser Diagram, Blender, category_groups.json, clean_joint_names.json, cond.npy, Stage 4: Feature Extraction, Stage 3: Joint Annotation, Stage 1: Motion Export (+22 more)

### Community 14 - "names_correct_llm.py"
Cohesion: 0.12
Nodes (14): correct_all(), _hips(), is_empty_entry(), is_non_empty_entry(), resolve_all(), append_id_list(), read_id_list(), save_json() (+6 more)

### Community 15 - "Multi-view Character Rendering"
Cohesion: 0.08
Nodes (17): find_motion_dirs(), find_shard_paths(), frame_mime_type(), is_render_complete(), load_frames_as_base64(), load_multiview_frames(), load_multiview_videos(), render_incomplete_reason() (+9 more)

### Community 16 - "LlamaRMSNorm"
Cohesion: 0.10
Nodes (8): DiTCrossBlock, LlamaRMSNorm, RoPEAttention, SwiGLUFFN, SpatioTemporalCrossBlock, TextCrossAttention, SpatialGraphSelfAttention, TemporalSelfAttention

### Community 17 - "Transformer Blocks"
Cohesion: 0.10
Nodes (6): UniMateFullCrossAttn, _apply_rotary_pos_emb(), GraphRoPE, RopeND, _rotate_half(), SpectralJointRoPE

### Community 18 - "Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx"
Cohesion: 0.07
Nodes (27): Bear (brown/black/polar), Bison, Buffalo/Water buffalo, Coyote/Jackal, Deer/Stag, Dire wolf, Dog, Donkey (+19 more)

### Community 19 - "motion_features.py"
Cohesion: 0.07
Nodes (20): atomic_output_path(), get_motion_clip_windows(), _activity_below_threshold(), _discontinuity_above_threshold(), _discontinuity_metrics(), extract_clip_feats(), _format_activity(), _format_discontinuity() (+12 more)

### Community 20 - "torch"
Cohesion: 0.08
Nodes (11): ClassifierFreeSampleModel, generate_samples(), build_overlap_keep_mask(), expand_motion_chain(), seed_expansion_x1(), build_keep_mask(), inbetween_sample_ode(), approx_standard_normal_cdf() (+3 more)

### Community 21 - "Text Embedding Precomputation"
Cohesion: 0.12
Nodes (14): b64_to_pil(), build_hint_footer(), build_multiview_intro(), build_view_header(), caption_rejection_reason(), gemini_client(), is_retryable_error(), openai_client() (+6 more)

### Community 22 - "normalize_scene"
Cohesion: 0.29
Nodes (4): get_root_objects(), get_scene_bbox(), get_scene_bbox_all_frames(), normalize_scene()

### Community 23 - "re"
Cohesion: 0.10
Nodes (16): _canon(), clean_japanese_name(), clean_joint_name(), clean_prefixed_name(), clean_spider_name(), clean_standard_name(), extract_side_prefix(), _looks_unmapped() (+8 more)

### Community 24 - "numpy"
Cohesion: 0.16
Nodes (13): plot_comparison(), plot_dataset(), _threshold_label(), _xlabel(), _joint_bins(), even_bins(), from_axis(), integer_bins() (+5 more)

### Community 25 - "plotting.py"
Cohesion: 0.05
Nodes (42): export_dir(), load_captions(), load_clip(), main(), _render_one(), tile(), _title(), _anchor_for_dir() (+34 more)

### Community 26 - "train_diffusion"
Cohesion: 0.04
Nodes (15): Quad10 rig release v1, run_download.sh script, Flow Matching, Graph-AdaLN Attention, Motion Library, TrainingTracker, _log_metrics(), main() (+7 more)

### Community 27 - "conditioning.py"
Cohesion: 0.05
Nodes (21): create_sample_condition(), _resolve_dataset(), create_train_dataloader(), _collect_scalar(), create_padded_matrix(), lengths_to_mask(), mixture_batch_collate(), _pad_joint_axis() (+13 more)

### Community 28 - "schema.py"
Cohesion: 0.12
Nodes (9): DatasetConfig, ExperimentConfig, MixamoConfig, ModelConfig, ObjaverseConfig, SamplingArgs, SchedulerConfig, TrainingConfig (+1 more)

### Community 29 - "caption_rewrite_llm.py"
Cohesion: 0.23
Nodes (7): generate_local(), generate_openai(), strip_llm_noise(), clean_answer(), load_json(), main(), validate()

### Community 30 - "Skeleton Alignment Utilities"
Cohesion: 0.10
Nodes (15): _blank_panel(), first_frame_positions(), _fit_height(), index_motion_npzs(), label_markers(), load_face_pairs(), main(), pair_forward() (+7 more)

### Community 31 - "LLM Client Interface"
Cohesion: 0.06
Nodes (16): model_joint_names(), create_text_encoder(), collect_texts(), encode_texts(), main(), parse_args(), resolve_roots(), get_logger() (+8 more)

### Community 32 - "Sampler"
Cohesion: 0.06
Nodes (3): ode, _fn(), sde

### Community 34 - "Blender Rigging Utilities"
Cohesion: 0.11
Nodes (3): UniMateDenoiserBase, UniMateFullAdaLN, UniMateGraphAdaLN

### Community 35 - "render_objaverse.py"
Cohesion: 0.15
Nodes (11): find_pending_stems(), main(), render_glb(), list_gltf_files(), load_excluded_stems(), get_expected_clip_dirs(), is_asset_render_skipped(), is_render_complete() (+3 more)

### Community 36 - "json"
Cohesion: 0.08
Nodes (11): load_map(), main(), load_json(), main(), main(), run_one(), sha256(), generate_matrix() (+3 more)

### Community 37 - "extract_features.py"
Cohesion: 0.08
Nodes (23): build_object_tasks(), _cache_params(), collect_object_npzs(), _digest(), discover_object_types(), _error_log_path(), _load_cached_result(), load_clip_trims() (+15 more)

### Community 38 - "Denoiser Model Variants"
Cohesion: 0.18
Nodes (9): _digit_runs(), empty_entry(), find_body_axis_pair(), find_symmetric_pair(), main(), _make_entry(), _match_pair_by_suffix(), resolve_face_joints() (+1 more)

### Community 39 - "dist_plot.py"
Cohesion: 0.13
Nodes (10): finish_figure(), label_for(), _log_tick_candidates(), mark_points(), panel_width_in(), pct_axis(), thin_log_ticks(), two_panel_figure() (+2 more)

### Community 40 - "names_clean_llm.py"
Cohesion: 0.13
Nodes (13): main(), main(), print_source_summary(), add_llm_args(), LLMClient, load_json(), build_user_prompt(), clean_all() (+5 more)

### Community 42 - "Generative Base Trainer"
Cohesion: 0.09
Nodes (13): _load_tpos_npz(), align_initial_facing(), align_root_to_ground(), align_root_xz_to_origin(), bfs_reorder_joints(), canonicalize_anim(), get_skeleton_diameter(), _normalize() (+5 more)

### Community 45 - "vis_tpose.py"
Cohesion: 0.19
Nodes (7): collect_keys_from_motions_dir(), default_single_output_path(), find_motion_npz(), load_tpose_from_npz(), main(), render_one(), save_skeleton_tpose_annotated()

### Community 46 - "Character Animation Scripts"
Cohesion: 0.13
Nodes (9): add_multi_gpu_args(), is_completed(), merge_shards(), detect_backend(), load_hints(), main(), parse_args(), _caption_prompt() (+1 more)

### Community 48 - "eval_foot_contact.py"
Cohesion: 0.17
Nodes (8): ContactJoints, evaluate_clip(), find_ground_contact_joints(), load_cond_dicts(), main(), parse_args(), resolve_object_type(), sweep()

### Community 49 - "mean_median_guides"
Cohesion: 0.25
Nodes (4): guide(), legend_loc_clear_of(), mean_median_guides(), x_frac()

### Community 50 - "render_action_multiview"
Cohesion: 0.12
Nodes (8): add_camera(), compose_frames_to_video(), enable_color_output(), fit_camera_distance(), get_scene_armatures(), remove_camera(), render_action_multiview(), _reset_frames_dir()

### Community 51 - "blender_render.py"
Cohesion: 0.12
Nodes (9): _create_light(), _gpu_lock_path(), gpu_render_lock(), load_armature(), load_file(), render_animation(), render_still(), setup_lighting() (+1 more)

### Community 52 - "math"
Cohesion: 0.23
Nodes (10): accessor(), load_glb(), main(), peak_summary(), quat_angle_deg(), rotation_stats(), vector_stats(), channel() (+2 more)

### Community 55 - "trainer.py"
Cohesion: 0.04
Nodes (18): betas_for_alpha_bar(), get_named_beta_schedule(), LossType, ModelMeanType, ModelVarType, mean_flat(), sum_flat(), space_timesteps() (+10 more)

### Community 56 - "load_and_prep_asset"
Cohesion: 0.14
Nodes (9): clear_normal_maps(), clear_scene(), find_meshes(), fix_materials(), keep_armature_meshes(), keep_main_mesh_only(), load_and_prep_asset(), set_materials_opaque() (+1 more)

### Community 57 - "GraphAttnBias"
Cohesion: 0.09
Nodes (5): DiTBlock, FinalLayer, compute_graph_bias(), GraphAttnBias, UniMateGraphCrossAttn

### Community 58 - "visualization.py"
Cohesion: 0.27
Nodes (4): save_skeleton_motion(), save_skeleton_motion_spectral(), _write_video(), visualize_and_save_motions()

### Community 59 - "vis_joint_count.py"
Cohesion: 0.11
Nodes (11): main(), parse_args(), print_table(), summarize(), configure_style(), load_int_map(), parse_int_list(), per_dataset_out_base() (+3 more)

### Community 61 - "Metadata I/O"
Cohesion: 0.17
Nodes (3): Logger, _CallerFileFormatter, zero_rank()

### Community 62 - "merge_extra_bone_weights"
Cohesion: 0.33
Nodes (3): build_ancestor_map(), merge_extra_bone_weights(), transfer_vertex_group()

### Community 64 - "recover_unimate_joint_pos_from_rot"
Cohesion: 0.16
Nodes (7): _augmented_global_positions(), fk_global_positions(), hml_rotations_to_bvh_quaternions(), recover_unimate_anim_from_rot(), recover_unimate_joint_pos_from_rot(), recover_unimate_root_quat_and_pos(), rotation_6d_to_matrix_np()

### Community 65 - "auto_label_unirig_quadruped_v2.original.py"
Cohesion: 0.18
Nodes (5): all_paths(), best_non_limb_path(), label_paw_branches(), lowest_path(), split_sides()

### Community 67 - "face_select_llm.py"
Cohesion: 0.10
Nodes (16): build_user_prompt(), _clean_side(), _format_section(), _hip_fields(), _is_complete(), parse_response(), prefilter_candidates(), resolve_rig() (+8 more)

### Community 68 - "plot_dataset"
Cohesion: 0.15
Nodes (12): _apply_clip(), main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize(), cdf_curve() (+4 more)

### Community 69 - "argparse"
Cohesion: 0.10
Nodes (14): parse_args(), main(), render_animated_file(), main(), render_clip_file(), main(), compute_directions(), default_output_path() (+6 more)

### Community 71 - "loguru"
Cohesion: 0.12
Nodes (6): Blender Python API (bpy), convert_character_to_glb(), convert_fbx_to_glb(), reset_scene(), parse_batch_args(), run_batch()

### Community 72 - "cougar_nopost"
Cohesion: 0.20
Nodes (10): assets, cougar_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names (+2 more)

### Community 73 - "_build_spectral_encoder"
Cohesion: 0.13
Nodes (3): _build_spectral_encoder(), SignNetSpectralEncoder, WIRESpectralEncoder

### Community 74 - "Matplotlib Ticker Formatting"
Cohesion: 0.20
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 77 - "baboon_nopost full-action feasibility test — 2026-11-04"
Cohesion: 0.40
Nodes (4): baboon_nopost full-action feasibility test — 2026-11-04, Exact prompts, Generation and QA facts, Scope and accounting

### Community 79 - "metadata.py"
Cohesion: 0.07
Nodes (19): main(), resolve_category_groups(), atomic_np_save(), build_stats(), check_metadata_object_types_consistent(), collect_captions(), compute_clip_windows(), _dict_get_ci() (+11 more)

### Community 82 - "goat_nopost"
Cohesion: 0.22
Nodes (9): goat_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names, source (+1 more)

### Community 83 - "Metadata Lookup Helpers"
Cohesion: 0.29
Nodes (7): AgentOps, CONSEJO.md, HANDOFF_LATEST.md, MEMORIA.md, SKILL.md, STATUS.md, WORKFLOW.md

### Community 84 - "hippopotamus_nopost"
Cohesion: 0.22
Nodes (9): hippopotamus_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names, source (+1 more)

### Community 86 - "render_tpose.py"
Cohesion: 0.16
Nodes (8): discover_assets(), main(), render_asset_tpose(), find_main_fbx(), sanitize_object_type(), compose_grid_2x2(), init_render_engine(), render_tpose_grid()

### Community 88 - "Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)"
Cohesion: 0.20
Nodes (9): 1. Criterio de Facing y Canonicalización, 2. Criterio de Texturas Embebidas, 3. Criterio de Ciclo Completo (2 Repeticiones), 4. Anclaje de Veredictos Visuales, Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets), Resumen Ejecutivo de Trazabilidad, Rutas de Archivos Verificadas por Asset, Tabla de Trazabilidad de los 28 Assets (+1 more)

### Community 90 - "Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs, Source Nodes

### Community 93 - "Cache Digest Utilities"
Cohesion: 0.50
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 97 - "cougar_nopost-jump-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_0-0.npy

### Community 113 - "cougar_nopost-jump-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_1-0.npy

### Community 147 - "os"
Cohesion: 0.16
Nodes (10): preprocess_asset(), _load(), main(), merge_summaries(), _save(), _scan_missing_frame_counts(), scan_clip_frames(), write_packed_images_to_dir() (+2 more)

### Community 148 - "cougar_nopost-run-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-run-rep_0-0.npy

### Community 150 - "Dramatic catalogue wave — generation and instrumental QA"
Cohesion: 0.33
Nodes (5): Dramatic catalogue wave — generation and instrumental QA, Exact prompts, Execution discipline and incidents, Raw evidence, Scope and status

### Community 152 - "cougar_nopost-run-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-run-rep_1-0.npy

### Community 154 - "goat_nopost-jump-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, goat_nopost-jump-rep_0-0.npy

### Community 155 - "goat_nopost-jump-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, goat_nopost-jump-rep_1-0.npy

### Community 156 - "goat_nopost-run-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, goat_nopost-run-rep_0-0.npy

### Community 157 - "goat_nopost-run-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, goat_nopost-run-rep_1-0.npy

### Community 158 - "hippopotamus_nopost-jump-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, hippopotamus_nopost-jump-rep_0-0.npy

### Community 159 - "hippopotamus_nopost-jump-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, hippopotamus_nopost-jump-rep_1-0.npy

### Community 160 - "hippopotamus_nopost-run-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, hippopotamus_nopost-run-rep_0-0.npy

### Community 161 - "hippopotamus_nopost-run-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, hippopotamus_nopost-run-rep_1-0.npy

### Community 162 - "Canary run+jump ~4 s — 2026-10-31"
Cohesion: 0.33
Nodes (5): Alcance y producción, Canary run+jump ~4 s — 2026-10-31, QA automático quad10, Rutas de evidencia, Simetría

### Community 163 - "anim_wave_20261102_dramatic_runner.sh"
Cohesion: 0.60
Nodes (4): qa_one(), anim_wave_20261102_dramatic_runner.sh script, variant_for_dir(), variants

### Community 165 - "samples"
Cohesion: 0.40
Nodes (4): format, motions_dir, runs, samples

### Community 172 - "Offline cranial-accessory annotation investigation — 2026-11-02"
Cohesion: 0.29
Nodes (6): Final rerun on the same ten GLBs, Finding, Offline cranial-accessory annotation investigation — 2026-11-02, Reuse decision, Scope and safety boundary, Targeted implementation

### Community 174 - "horse_nopost catalogue-verb feasibility test — 2026-11-02"
Cohesion: 0.33
Nodes (5): Exact prompts, Generation and QA accounting, horse_nopost catalogue-verb feasibility test — 2026-11-02, Raw instrumental numbers, Scope and hypothesis

### Community 177 - "Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?, Source Nodes

### Community 178 - "run_initial_wave.sh"
Cohesion: 0.83
Nodes (3): check_rig(), qa_one(), run_initial_wave.sh script

### Community 179 - "deer_nopost full-action feasibility test — 2026-11-02"
Cohesion: 0.33
Nodes (5): deer_nopost full-action feasibility test — 2026-11-02, Exact prompts, Generation and QA facts, Orchestration incident and recovery, Scope and accounting

### Community 189 - "2026-11-02 21:55 +03:00 — dramatic catalogue wave started"
Cohesion: 0.06
Nodes (32): 2026-11-02 21:44 +03:00 — horse_nopost catalogue-verb feasibility test, 2026-11-02 21:47 +03:00 — dog canary plumbing failure caught pre-sampling, 2026-11-02 21:47 +03:00 — preflight passed; dog canary released, 2026-11-02 21:51 +03:00 — dog canary 1/2 QA complete, 2026-11-02 21:52 +03:00 — dog canary gate passed; remainder released, 2026-11-02 21:53 +03:00 — remainder input gate complete, 2026-11-02 21:55 +03:00 — dramatic catalogue wave started, 2026-11-02 22:04 +03:00 — remainder sampling progress (+24 more)

## Knowledge Gaps
- **25 isolated node(s):** `variants`, `graphify`, `FFmpeg`, `UniML3D Teaser Diagram`, `Stage 5: Mesh Animation` (+20 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1380 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **89 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Data Process README` connect `Denoiser Base Class` to `train_diffusion`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **What connects `variants`, `graphify`, `FFmpeg` to the rest of the system?**
  _25 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `preprocess_char.py` be split into smaller, more focused modules?**
  _Cohesion score 0.040211147337369975 - nodes in this community are weakly interconnected._
- **Should `blender_export.py` be split into smaller, more focused modules?**
  _Cohesion score 0.047593865679534636 - nodes in this community are weakly interconnected._
- **Should `numpy` be split into smaller, more focused modules?**
  _Cohesion score 0.11396011396011396 - nodes in this community are weakly interconnected._
- **Should `motion_utils.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12554112554112554 - nodes in this community are weakly interconnected._
- **Should `sample.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05593561368209256 - nodes in this community are weakly interconnected._