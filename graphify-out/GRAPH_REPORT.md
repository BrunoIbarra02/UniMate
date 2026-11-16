# Graph Report - UniMate  (2026-11-04)

## Corpus Check
- 506 files · ~336,965 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 273 file(s) not represented in the graph (top: .log 256, .fbx 8, .tsv 7)

## Summary
- 2786 nodes · 5758 edges · 211 communities (106 shown, 105 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 122 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `021b8ceb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- mesh_animation/common.py
- blender_export.py
- numpy
- motion_utils.py
- sample.py
- patch_annotations.py
- sys
- topology.py
- animate_lbs.py
- ICPlan
- Diffusion Planning Math
- auto_label_unirig_quadruped_v2.py
- T5Conditioner
- Denoiser Base Class
- face_select_llm.py
- Multi-view Character Rendering
- LlamaRMSNorm
- Transformer Blocks
- Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx
- motion_features.py
- torch
- Text Embedding Precomputation
- normalize_scene
- re
- dist_plot.py
- plotting.py
- train_diffusion
- create_sample_condition
- schema.py
- Transport
- Skeleton Alignment Utilities
- LLM Client Interface
- Sampler
- blocks/common.py
- torch
- json
- extract_features.py
- Denoiser Model Variants
- caption_batch
- main
- Sampler
- Generative Base Trainer
- T5 Text Conditioner
- GaussianDiffusion
- vis_tpose.py
- Character Animation Scripts
- Joint Distribution Visualization
- eval_foot_contact.py
- mean_median_guides
- kinematics.py
- blender_render.py
- math
- vis_caption.py
- atomic_output_path
- trainer.py
- patch_joint_labels
- SpatioTemporalBlock
- time
- vis_joint_count.py
- MotionDataset
- Metadata I/O
- blender_rig.py
- argparse
- auto_label_unirig_quadruped_v2.original.py
- Blender Python API (bpy)
- names_correct_llm.py
- plot_dataset
- vis_motion.py
- BERT and CLIP Encoders
- loguru
- cougar_nopost
- ._build_text_embeddings
- Matplotlib Ticker Formatting
- baboon_nopost full-action feasibility test — 2026-11-04
- Export Resume Markers
- metadata.py
- get_object_metadata
- load_json
- goat_nopost
- Metadata Lookup Helpers
- hippopotamus_nopost
- wave5_supervisor.sh
- render_tpose.py
- .__init__
- Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)
- BERTConditioner
- Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs
- wave5_validate_profiles.sh
- Cache Digest Utilities
- load_and_canonicalize_motion
- wave5_walk_one.sh
- reorder_anim_bfs
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
- preprocess_char.py
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
- MixtureSampler
- detect_backend
- run_canary_4s.sh
- continue_canary_4s.sh
- probe_results.sh
- rerender_24fps.sh
- Offline cranial-accessory annotation investigation — 2026-11-02
- _cache_params
- horse_nopost catalogue-verb feasibility test — 2026-11-02
- wave7_species_runner.sh
- Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?
- run_initial_wave.sh
- deer_nopost full-action feasibility test — 2026-11-02
- compute_graph_bias
- summarize_cranial.py
- run_rig_wave_profiles.sh
- wave7_preflight_remote.sh
- run_offline_eval.sh
- run_hippo_wallow_fallback.sh
- prepare_rig_wave.sh
- run_walk_variants.sh
- 2026-11-02 21:55 +03:00 — dramatic catalogue wave started
- .wave9_check_fresh.sh
- anim_wave_20261102_deer_catalogue_runner.sh
- anim_wave_20261102_horse_catalogue_runner.sh
- .wave9_check_inference_remote.sh
- .wave9_deep_worker_check.sh
- .wave9_exact_prior_paths.sh
- .wave9_first_output_check.sh
- .wave9_inference_monitor.sh
- .wave9_launch_inference.sh
- .wave9_launch_inference_remote.sh
- .wave9_launch_prepare_remote.sh
- .wave9_launch_progress_monitor_remote.sh
- .wave9_monitor.sh
- .wave9_prepare.sh
- .wave9_progress_monitor_remote.sh
- .wave9_remote_find_scripts.sh
- .wave9_remote_inspect.sh
- .wave9_remote_read_templates.sh
- .wave9_validate_manifest_remote.sh
- .wave9_validate_profiles.sh
- .wave9_walk_one.sh

## God Nodes (most connected - your core abstractions)
1. `MotionDataset` - 38 edges
2. `GaussianDiffusion` - 37 edges
3. `2026-11-02 21:55 +03:00 — dramatic catalogue wave started` - 35 edges
4. `MainConfig` - 30 edges
5. `Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx` - 27 edges
6. `train_diffusion()` - 26 edges
7. `UniMateDenoiserBase` - 24 edges
8. `plot_dataset()` - 23 edges
9. `export_asset()` - 20 edges
10. `plot_comparison()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Data Process README` --references--> `UniML3D Teaser Diagram`  [EXTRACTED]
  data_process/README.md → assets/teaser.png
- `build_anim_from_npy()` --calls--> `recover_unimate_joint_pos_from_ric()`  [EXTRACTED]
  data_process/mesh_animation/animate_motion.py → unimate/utils/motion_utils.py
- `visualize_and_save_motions()` --calls--> `render_skeleton_tpose()`  [EXTRACTED]
  unimate/utils/visualization.py → data_process/utils/plotting.py
- `visualize_and_save_motions()` --calls--> `render_skeleton_tpos_spectral()`  [EXTRACTED]
  unimate/utils/visualization.py → data_process/utils/plotting.py
- `visualize_and_save_motions()` --calls--> `save_skeleton_motion()`  [EXTRACTED]
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

## Communities (211 total, 105 thin omitted)

### Community 0 - "mesh_animation/common.py"
Cohesion: 0.11
Nodes (13): _action_bone_names(), _adopt_action(), animate_character_fbx(), load_motion_local_mats(), animate_character(), build_anims_from_export_npz(), clip_output_path(), load_character() (+5 more)

### Community 1 - "blender_export.py"
Cohesion: 0.04
Nodes (35): action_is_relevant_pose(), _apply_root_rotation(), build_rest_animation(), build_skeleton_arrays(), build_vertex_groups_sparse(), build_vgroup_to_bone_mapping(), children_from_parents(), choose_main_armature() (+27 more)

### Community 2 - "numpy"
Cohesion: 0.07
Nodes (23): apply_joint_addition_ellipsoid(), apply_joint_addition_linear(), apply_joint_perturbation(), apply_joint_removal(), apply_skeleton_pooling(), bone_length_weighted_sample(), build_children_map(), collapse_single_child_joint() (+15 more)

### Community 3 - "motion_utils.py"
Cohesion: 0.10
Nodes (11): _augmented_global_positions(), recompute_position_features(), compute_cont6d_params(), compute_local_velocity(), compute_rifke(), compute_rots_from_tpos(), compute_unimate_motion_feats(), fk_global_positions() (+3 more)

### Community 4 - "sample.py"
Cohesion: 0.06
Nodes (27): create_dataset(), build_joint_keep_mask(), get_joint_names(), parse_keep_joints(), parse_keep_frames(), _encode_prompt(), _gt_valid_lengths(), InferenceArgs (+19 more)

### Community 5 - "patch_annotations.py"
Cohesion: 0.10
Nodes (20): apply_root_offsets(), load_json(), load_overrides(), load_rig_flags(), main(), normalize_locomotion(), object_type_of(), patch_captions() (+12 more)

### Community 6 - "sys"
Cohesion: 0.08
Nodes (27): export_asset(), list_asset_files(), main(), parse_args(), pick_importer(), export_mixamo(), main(), export_objaverse() (+19 more)

### Community 7 - "topology.py"
Cohesion: 0.10
Nodes (13): _adjacency_list(), _build_kinchains(), _build_laplacian(), _children_map(), compute_adjacency_matrix(), compute_edge_indexs(), compute_edge_relations_and_distances(), compute_joint_depths() (+5 more)

### Community 8 - "animate_lbs.py"
Cohesion: 0.13
Nodes (12): animate_lbs(), extract_skin(), lbs_deform(), motion_from_canonical_char(), save_obj_sequence(), drive_and_export(), quat_pos_to_mats(), compute_bone_keyframes() (+4 more)

### Community 9 - "ICPlan"
Cohesion: 0.07
Nodes (4): expand_t_like_x(), GVPCPlan, ICPlan, VPCPlan

### Community 10 - "Diffusion Planning Math"
Cohesion: 0.10
Nodes (17): add_qwen_model_args(), load_qwen_model(), qwen_generate(), save_json(), aggregate_votes(), build_messages(), classify_asset(), classify_batch() (+9 more)

### Community 11 - "auto_label_unirig_quadruped_v2.py"
Cohesion: 0.11
Nodes (9): all_paths(), best_non_limb_path(), cranial_coordinates(), is_central_muzzle(), is_mirrored_ear_pair(), label_paw_branches(), lowest_path(), simple_chain() (+1 more)

### Community 12 - "T5Conditioner"
Cohesion: 0.08
Nodes (6): BaseConditioner, _hash_trick(), _length_to_mask(), T5Conditioner, TorchAutocast, WhiteSpaceTokenizer

### Community 13 - "Denoiser Base Class"
Cohesion: 0.07
Nodes (30): UniML3D Teaser Diagram, Blender, category_groups.json, clean_joint_names.json, cond.npy, Stage 4: Feature Extraction, Stage 3: Joint Annotation, Stage 1: Motion Export (+22 more)

### Community 14 - "face_select_llm.py"
Cohesion: 0.09
Nodes (22): correct_all(), _hips(), is_empty_entry(), is_non_empty_entry(), main(), build_user_prompt(), _format_section(), _is_complete() (+14 more)

### Community 15 - "Multi-view Character Rendering"
Cohesion: 0.09
Nodes (9): find_motion_dirs(), find_shard_paths(), frame_mime_type(), is_render_complete(), load_frames_as_base64(), openai_client(), select_frame_paths(), shard_output_path() (+1 more)

### Community 16 - "LlamaRMSNorm"
Cohesion: 0.08
Nodes (10): DiTBlock, FinalLayer, LlamaRMSNorm, modulate(), RoPEAttention, SwiGLUFFN, SpatioTemporalCrossBlock, TextCrossAttention (+2 more)

### Community 17 - "Transformer Blocks"
Cohesion: 0.07
Nodes (8): _apply_rotary_pos_emb(), _build_spectral_encoder(), GraphRoPE, RopeND, _rotate_half(), SignNetSpectralEncoder, SpectralJointRoPE, WIRESpectralEncoder

### Community 18 - "Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx"
Cohesion: 0.07
Nodes (27): Bear (brown/black/polar), Bison, Buffalo/Water buffalo, Coyote/Jackal, Deer/Stag, Dire wolf, Dog, Donkey (+19 more)

### Community 19 - "motion_features.py"
Cohesion: 0.10
Nodes (14): compute_clip_windows(), get_motion_clip_windows(), _activity_below_threshold(), _discontinuity_above_threshold(), _discontinuity_metrics(), extract_clip_feats(), _format_activity(), _format_discontinuity() (+6 more)

### Community 20 - "torch"
Cohesion: 0.12
Nodes (7): ClassifierFreeSampleModel, generate_samples(), build_overlap_keep_mask(), expand_motion_chain(), seed_expansion_x1(), build_keep_mask(), inbetween_sample_ode()

### Community 21 - "Text Embedding Precomputation"
Cohesion: 0.15
Nodes (11): b64_to_pil(), build_hint_footer(), build_multiview_intro(), build_view_header(), gemini_client(), is_retryable_error(), _build_openai_messages(), _build_qwen_messages() (+3 more)

### Community 22 - "normalize_scene"
Cohesion: 0.29
Nodes (4): get_root_objects(), get_scene_bbox(), get_scene_bbox_all_frames(), normalize_scene()

### Community 23 - "re"
Cohesion: 0.10
Nodes (15): build_user_prompt(), main(), _canon(), clean_japanese_name(), clean_prefixed_name(), clean_spider_name(), clean_standard_name(), extract_side_prefix() (+7 more)

### Community 24 - "dist_plot.py"
Cohesion: 0.10
Nodes (21): plot_comparison(), plot_dataset(), _threshold_label(), _xlabel(), display_name(), even_bins(), finish_figure(), from_axis() (+13 more)

### Community 25 - "plotting.py"
Cohesion: 0.06
Nodes (39): _anchor_for_dir(), _annotate_joints(), _as_xyz(), _box_aspect_from_bounds(), _capture_rgb(), _cubic_bounds(), _draw_caption(), _draw_static_skeleton() (+31 more)

### Community 26 - "train_diffusion"
Cohesion: 0.04
Nodes (14): Quad10 rig release v1, run_download.sh script, Flow Matching, Graph-AdaLN Attention, create_train_dataloader(), TrainingTracker, _log_metrics(), _resume_from_checkpoint() (+6 more)

### Community 27 - "create_sample_condition"
Cohesion: 0.15
Nodes (8): create_sample_condition(), _resolve_dataset(), apply_cropping(), apply_normalization(), apply_padding(), build_parent_features(), extract_conditions(), realign_unimate_clip()

### Community 28 - "schema.py"
Cohesion: 0.06
Nodes (14): DatasetConfig, ExperimentConfig, MainConfig, MixamoConfig, ModelConfig, ObjaverseConfig, SamplingArgs, SchedulerConfig (+6 more)

### Community 30 - "Skeleton Alignment Utilities"
Cohesion: 0.09
Nodes (14): _blank_panel(), first_frame_positions(), _fit_height(), index_motion_npzs(), label_markers(), load_face_pairs(), main(), pair_forward() (+6 more)

### Community 31 - "LLM Client Interface"
Cohesion: 0.11
Nodes (13): encode_texts(), main(), parse_args(), resolve_roots(), get_logger(), cache_path(), load_cache(), load_caches() (+5 more)

### Community 32 - "Sampler"
Cohesion: 0.09
Nodes (3): ode, _fn(), sde

### Community 33 - "blocks/common.py"
Cohesion: 0.11
Nodes (7): UniMateDenoiserBase, build_graph_bias_params(), GraphAttnBias, UniMateFullAdaLN, UniMateFullCrossAttn, UniMateGraphAdaLN, UniMateGraphCrossAttn

### Community 35 - "torch"
Cohesion: 0.16
Nodes (8): _collect_scalar(), create_padded_matrix(), lengths_to_mask(), mixture_batch_collate(), _pad_joint_axis(), approx_standard_normal_cdf(), discretized_gaussian_log_likelihood(), normal_kl()

### Community 36 - "json"
Cohesion: 0.11
Nodes (12): strip_llm_noise(), load_map(), main(), clean_answer(), load_json(), main(), validate(), load_json() (+4 more)

### Community 37 - "extract_features.py"
Cohesion: 0.14
Nodes (14): build_object_tasks(), collect_object_npzs(), discover_object_types(), load_clip_trims(), load_filtered_objects(), _object_part_path(), read_root_offsets(), resolve_activity_keep_path() (+6 more)

### Community 38 - "Denoiser Model Variants"
Cohesion: 0.12
Nodes (13): _clean_side(), _hip_fields(), parse_response(), _validate_sides(), _digit_runs(), empty_entry(), find_body_axis_pair(), find_symmetric_pair() (+5 more)

### Community 39 - "caption_batch"
Cohesion: 0.16
Nodes (10): caption_rejection_reason(), load_multiview_frames(), load_multiview_videos(), render_incomplete_reason(), uniform_subsample(), _view_label_from_id(), generate_openai(), generate_qwen() (+2 more)

### Community 40 - "main"
Cohesion: 0.12
Nodes (9): _error_log_path(), _load_cached_result(), main(), _params_hash(), process_object_task(), _prune_object_clips(), resolve_category_groups(), build_stats() (+1 more)

### Community 41 - "Sampler"
Cohesion: 0.09
Nodes (4): _build_diffusion(), create_diffusion(), create_transport(), Sampler

### Community 42 - "Generative Base Trainer"
Cohesion: 0.12
Nodes (11): align_initial_facing(), align_root_to_ground(), align_root_xz_to_origin(), canonicalize_anim(), get_root_facing_quat(), get_skeleton_diameter(), _normalize(), scale_anim() (+3 more)

### Community 44 - "GaussianDiffusion"
Cohesion: 0.06
Nodes (3): _extract_into_tensor(), GaussianDiffusion, get_model_output()

### Community 45 - "vis_tpose.py"
Cohesion: 0.19
Nodes (7): collect_keys_from_motions_dir(), default_single_output_path(), find_motion_npz(), load_tpose_from_npz(), main(), render_one(), save_skeleton_tpose_annotated()

### Community 46 - "Character Animation Scripts"
Cohesion: 0.12
Nodes (10): add_multi_gpu_args(), is_completed(), merge_shards(), detect_backend(), image_params(), load_hints(), main(), parse_args() (+2 more)

### Community 48 - "eval_foot_contact.py"
Cohesion: 0.16
Nodes (10): _validate_motion(), ContactJoints, evaluate_clip(), find_ground_contact_joints(), load_cond_dicts(), main(), parse_args(), resolve_object_type() (+2 more)

### Community 49 - "mean_median_guides"
Cohesion: 0.25
Nodes (4): guide(), legend_loc_clear_of(), mean_median_guides(), x_frac()

### Community 50 - "kinematics.py"
Cohesion: 0.22
Nodes (6): clip_global(), fk(), frame_global(), qmul(), qrot(), rest_global()

### Community 51 - "blender_render.py"
Cohesion: 0.05
Nodes (40): main(), render_animated_file(), find_pending_stems(), main(), render_glb(), main(), render_clip_file(), discover_pose_actions() (+32 more)

### Community 52 - "math"
Cohesion: 0.23
Nodes (10): accessor(), load_glb(), main(), peak_summary(), quat_angle_deg(), rotation_stats(), vector_stats(), channel() (+2 more)

### Community 53 - "vis_caption.py"
Cohesion: 0.26
Nodes (7): export_dir(), load_captions(), load_clip(), main(), _render_one(), tile(), _title()

### Community 54 - "atomic_output_path"
Cohesion: 0.18
Nodes (6): atomic_np_save(), atomic_output_path(), collect_captions(), save_json(), save_metadata_report(), save_outputs()

### Community 55 - "trainer.py"
Cohesion: 0.07
Nodes (12): betas_for_alpha_bar(), get_named_beta_schedule(), LossType, ModelMeanType, ModelVarType, mean_flat(), sum_flat(), ModelType (+4 more)

### Community 56 - "patch_joint_labels"
Cohesion: 0.20
Nodes (8): needs_side_from_x(), patch_joint_labels(), raw_side(), relabel_chains(), rig_npz(), side_from_x(), split_side(), unify_root_labels()

### Community 58 - "time"
Cohesion: 0.31
Nodes (3): main(), run_one(), sha256()

### Community 59 - "vis_joint_count.py"
Cohesion: 0.09
Nodes (13): main(), parse_args(), print_table(), summarize(), configure_style(), label_for(), load_int_map(), parse_int_list() (+5 more)

### Community 61 - "Metadata I/O"
Cohesion: 0.17
Nodes (3): Logger, _CallerFileFormatter, zero_rank()

### Community 62 - "blender_rig.py"
Cohesion: 0.10
Nodes (13): _add_fcurves(), build_ancestor_map(), delete_dominant_weighted_vertices(), delete_skin_vertices_for_bones(), export_selected_to_file(), find_skinned_meshes(), _find_upstream_image_node(), merge_extra_bone_weights() (+5 more)

### Community 64 - "argparse"
Cohesion: 0.10
Nodes (16): parse_args(), parse_args(), parse_args(), animate_character(), build_anim_from_npy(), build_anim_from_npz(), load_animation(), load_cond_data() (+8 more)

### Community 65 - "auto_label_unirig_quadruped_v2.original.py"
Cohesion: 0.18
Nodes (5): all_paths(), best_non_limb_path(), label_paw_branches(), lowest_path(), split_sides()

### Community 67 - "names_correct_llm.py"
Cohesion: 0.09
Nodes (17): _alarm_handler(), FatalLLMError, generate_local(), generate_openai(), install_rig_alarm(), RigTimeout, uninstall_rig_alarm(), clean_rig() (+9 more)

### Community 68 - "plot_dataset"
Cohesion: 0.13
Nodes (12): _apply_clip(), _joint_bins(), main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize() (+4 more)

### Community 69 - "vis_motion.py"
Cohesion: 0.31
Nodes (4): compute_directions(), default_output_path(), load_motion_from_npz(), main()

### Community 70 - "BERT and CLIP Encoders"
Cohesion: 0.17
Nodes (3): space_timesteps(), SpacedDiffusion, _WrappedModel

### Community 71 - "loguru"
Cohesion: 0.21
Nodes (6): convert_character_to_glb(), convert_fbx_to_glb(), import_fbx(), reset_scene(), parse_batch_args(), run_batch()

### Community 72 - "cougar_nopost"
Cohesion: 0.20
Nodes (10): assets, cougar_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names (+2 more)

### Community 74 - "Matplotlib Ticker Formatting"
Cohesion: 0.20
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 77 - "baboon_nopost full-action feasibility test — 2026-11-04"
Cohesion: 0.40
Nodes (4): baboon_nopost full-action feasibility test — 2026-11-04, Exact prompts, Generation and QA facts, Scope and accounting

### Community 79 - "metadata.py"
Cohesion: 0.19
Nodes (8): load_all_metadata(), load_category_groups(), load_clean_joint_names(), load_face_joint_names(), load_joint_names(), load_json(), load_motion_captions(), print_summary()

### Community 80 - "get_object_metadata"
Cohesion: 0.33
Nodes (3): _dict_get_ci(), get_object_face_joints(), get_object_metadata()

### Community 81 - "load_json"
Cohesion: 0.14
Nodes (5): flatten_rgba(), load_json(), _record(), ExportEvidence, _has_word()

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
Cohesion: 0.10
Nodes (12): discover_assets(), main(), render_asset_tpose(), find_main_fbx(), sanitize_object_type(), truebones_clip_name(), build_transformation_mat(), camera_pose_on_sphere() (+4 more)

### Community 87 - ".__init__"
Cohesion: 0.15
Nodes (3): DiTCrossBlock, InputLayer, TimestepEmbedder

### Community 88 - "Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)"
Cohesion: 0.20
Nodes (9): 1. Criterio de Facing y Canonicalización, 2. Criterio de Texturas Embebidas, 3. Criterio de Ciclo Completo (2 Repeticiones), 4. Anclaje de Veredictos Visuales, Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets), Resumen Ejecutivo de Trazabilidad, Rutas de Archivos Verificadas por Asset, Tabla de Trazabilidad de los 28 Assets (+1 more)

### Community 89 - "BERTConditioner"
Cohesion: 0.14
Nodes (4): BERTConditioner, CLIPConditioner, create_text_encoder(), get_text_encoder_dim()

### Community 90 - "Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs, Source Nodes

### Community 93 - "Cache Digest Utilities"
Cohesion: 0.50
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 94 - "load_and_canonicalize_motion"
Cohesion: 0.33
Nodes (3): load_and_canonicalize_motion(), _load_npz_anim(), _names_permutation()

### Community 96 - "reorder_anim_bfs"
Cohesion: 0.33
Nodes (3): _load_tpos_npz(), bfs_reorder_joints(), reorder_anim_bfs()

### Community 97 - "cougar_nopost-jump-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_0-0.npy

### Community 113 - "cougar_nopost-jump-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_1-0.npy

### Community 147 - "os"
Cohesion: 0.16
Nodes (11): _load(), main(), merge_summaries(), _save(), _scan_missing_frame_counts(), scan_clip_frames(), _asset_marker_path(), collect_joint_names_from_markers() (+3 more)

### Community 148 - "cougar_nopost-run-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-run-rep_0-0.npy

### Community 149 - "preprocess_char.py"
Cohesion: 0.10
Nodes (12): clean_joint_name(), bake_canonical_asset(), cond_from_rest(), preprocess_asset(), _umeyama(), bind_action(), clear_animation_state(), deselect() (+4 more)

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

### Community 175 - "wave7_species_runner.sh"
Cohesion: 0.83
Nodes (3): qa_one(), read_config(), wave7_species_runner.sh script

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
Cohesion: 0.05
Nodes (38): 2026-11-02 21:44 +03:00 — horse_nopost catalogue-verb feasibility test, 2026-11-02 21:47 +03:00 — dog canary plumbing failure caught pre-sampling, 2026-11-02 21:47 +03:00 — preflight passed; dog canary released, 2026-11-02 21:51 +03:00 — dog canary 1/2 QA complete, 2026-11-02 21:52 +03:00 — dog canary gate passed; remainder released, 2026-11-02 21:53 +03:00 — remainder input gate complete, 2026-11-02 21:55 +03:00 — dramatic catalogue wave started, 2026-11-02 22:04 +03:00 — remainder sampling progress (+30 more)

## Knowledge Gaps
- **25 isolated node(s):** `variants`, `graphify`, `FFmpeg`, `UniML3D Teaser Diagram`, `Stage 5: Mesh Animation` (+20 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1427 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **105 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MotionDataset` connect `MotionDataset` to `numpy`, `motion_utils.py`, `create_sample_condition`, `._build_text_embeddings`, `T5 Text Conditioner`, `._batch_encode_unique`, `._apply_augmentations`, `.save_dataset_stats`, `.__init__`, `._split_names`, `LLM Client Interface`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **What connects `variants`, `graphify`, `FFmpeg` to the rest of the system?**
  _25 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `mesh_animation/common.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10606060606060606 - nodes in this community are weakly interconnected._
- **Why does `Sampler` connect `Sampler` to `Sampler`, `sample.py`, `trainer.py`, `train_diffusion`, `schema.py`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Should `blender_export.py` be split into smaller, more focused modules?**
  _Cohesion score 0.044642857142857144 - nodes in this community are weakly interconnected._
- **Why does `GaussianDiffusion` connect `GaussianDiffusion` to `BERT and CLIP Encoders`, `trainer.py`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Should `numpy` be split into smaller, more focused modules?**
  _Cohesion score 0.06734006734006734 - nodes in this community are weakly interconnected._