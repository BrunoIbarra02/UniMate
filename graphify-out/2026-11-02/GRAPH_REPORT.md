# Graph Report - UniMate  (2026-11-02)

## Corpus Check
- 435 files · ~278,487 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 262 file(s) not represented in the graph (top: .log 246, .fbx 8, .tsv 6)

## Summary
- 2658 nodes · 5615 edges · 193 communities (101 shown, 92 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 122 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `021b8ceb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- preprocess_char.py
- blender_export.py
- dataset.py
- conditioning.py
- sample.py
- patch_annotations.py
- torch
- topology.py
- t5.py
- Blender Rendering Utilities
- Diffusion Planning Math
- auto_label_unirig_quadruped_v2.py
- T5Conditioner
- Denoiser Base Class
- names_clean_llm.py
- Multi-view Character Rendering
- LlamaRMSNorm
- Transformer Blocks
- Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx
- motion_features.py
- gaussian_diffusion.py
- Text Embedding Precomputation
- names_clean_llm.py
- re
- GaussianDiffusion
- render_skeleton_motion_spectral
- train_diffusion
- torch
- Motion Feature Extraction
- llm.py
- Skeleton Alignment Utilities
- LLM Client Interface
- Sampler
- blocks/common.py
- Blender Rigging Utilities
- pathlib
- plotting.py
- extract_features.py
- Denoiser Model Variants
- value_axis
- render_action_multiview
- ODE Sampling Integrators
- Generative Base Trainer
- T5 Text Conditioner
- _extract_into_tensor
- json
- Character Animation Scripts
- Joint Distribution Visualization
- is_canonical_label
- Mesh Animation Plumbing
- Frame Count Visualization
- load_and_prep_asset
- math
- .__init__
- Transport
- expand_t_like_x
- GraphAttnBias
- Blender Action Management
- Plotting Bin Helpers
- os
- Metadata I/O
- main
- render_tpose_grid
- blender_export.py
- auto_label_unirig_quadruped_v2.original.py
- augmentations.py
- topology_utils.py
- plot_dataset
- Diffusion Loop Utilities
- BERT and CLIP Encoders
- argparse
- cougar_nopost
- Train-Eval Splitting
- Matplotlib Ticker Formatting
- save_skeleton_motion
- Export Resume Markers
- metadata.py
- Plot Legend Helpers
- Diffusion Training Losses
- goat_nopost
- Metadata Lookup Helpers
- hippopotamus_nopost
- process_object
- sde
- InputLayer
- Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)
- _build_spectral_encoder
- Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs
- dataset/factory.py
- GVPCPlan
- Cache Digest Utilities
- atomic_output_path
- flatten_rgba
- ndarray
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
- mean_median_guides
- _capture_rgb
- cougar_nopost-run-rep_0-0.npy
- unique_labels
- VPCPlan
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
- blender_render.py
- setup_lighting
- samples
- get_object_metadata
- MotionDataset
- run_canary_4s.sh
- continue_canary_4s.sh
- probe_results.sh
- rerender_24fps.sh
- Offline cranial-accessory annotation investigation — 2026-11-02
- reorder_anim_bfs
- horse_nopost catalogue-verb feasibility test — 2026-11-02
- load_armature
- SpatioTemporalBlock
- Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?
- run_initial_wave.sh
- deer_nopost full-action feasibility test — 2026-11-02
- TimestepEmbedder
- _UnconditionalWrapper
- run_rig_wave_profiles.sh
- _cache_params
- run_offline_eval.sh
- run_hippo_wallow_fallback.sh
- prepare_rig_wave.sh
- run_walk_variants.sh
- Codex session log
- percentile_stats
- anim_wave_20261102_deer_catalogue_runner.sh
- anim_wave_20261102_horse_catalogue_runner.sh

## God Nodes (most connected - your core abstractions)
1. `MotionDataset` - 38 edges
2. `GaussianDiffusion` - 37 edges
3. `MainConfig` - 30 edges
4. `Per-species action catalogue -- extracted verbatim from animal_creature_3d_animation_catalogue.docx` - 27 edges
5. `train_diffusion()` - 26 edges
6. `UniMateDenoiserBase` - 24 edges
7. `plot_dataset()` - 23 edges
8. `export_asset()` - 20 edges
9. `plot_comparison()` - 20 edges
10. `plot_dataset()` - 20 edges

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

## Communities (193 total, 92 thin omitted)

### Community 0 - "preprocess_char.py"
Cohesion: 0.05
Nodes (30): bake_canonical_asset(), cond_from_rest(), preprocess_asset(), _umeyama(), _apply_root_rotation(), apply_zup_to_yup(), bind_action(), build_rest_animation() (+22 more)

### Community 1 - "blender_export.py"
Cohesion: 0.09
Nodes (28): export_asset(), list_asset_files(), main(), parse_args(), pick_importer(), export_mixamo(), main(), parse_args() (+20 more)

### Community 2 - "dataset.py"
Cohesion: 0.08
Nodes (16): _augmented_global_positions(), create_condition(), _validate_motion(), compute_cont6d_params(), compute_local_velocity(), compute_rifke(), compute_rots_from_tpos(), compute_unimate_motion_feats() (+8 more)

### Community 3 - "conditioning.py"
Cohesion: 0.16
Nodes (7): create_sample_condition(), _resolve_dataset(), apply_cropping(), apply_normalization(), apply_padding(), build_parent_features(), extract_conditions()

### Community 4 - "sample.py"
Cohesion: 0.06
Nodes (27): MainConfig, create_dataset(), build_joint_keep_mask(), get_joint_names(), parse_keep_joints(), parse_keep_frames(), _build_diffusion(), _encode_prompt() (+19 more)

### Community 5 - "patch_annotations.py"
Cohesion: 0.06
Nodes (34): apply_root_offsets(), load_json(), load_overrides(), load_rig_flags(), main(), needs_side_from_x(), normalize_locomotion(), object_type_of() (+26 more)

### Community 6 - "torch"
Cohesion: 0.09
Nodes (8): ClassifierFreeSampleModel, generate_samples(), build_overlap_keep_mask(), expand_motion_chain(), seed_expansion_x1(), build_keep_mask(), inbetween_sample_ode(), get_logger()

### Community 7 - "topology.py"
Cohesion: 0.10
Nodes (14): build_topology_cond(), _adjacency_list(), _build_kinchains(), _build_laplacian(), _children_map(), compute_adjacency_matrix(), compute_edge_indexs(), compute_edge_relations_and_distances() (+6 more)

### Community 10 - "Diffusion Planning Math"
Cohesion: 0.08
Nodes (21): add_qwen_model_args(), load_json(), load_qwen_model(), qwen_generate(), save_json(), _record(), aggregate_votes(), build_messages() (+13 more)

### Community 11 - "auto_label_unirig_quadruped_v2.py"
Cohesion: 0.11
Nodes (9): all_paths(), best_non_limb_path(), cranial_coordinates(), is_central_muzzle(), is_mirrored_ear_pair(), label_paw_branches(), lowest_path(), simple_chain() (+1 more)

### Community 12 - "T5Conditioner"
Cohesion: 0.09
Nodes (5): BaseConditioner, _length_to_mask(), T5Conditioner, TorchAutocast, WhiteSpaceTokenizer

### Community 13 - "Denoiser Base Class"
Cohesion: 0.05
Nodes (34): Quad10 rig release v1, UniML3D Teaser Diagram, Blender, category_groups.json, clean_joint_names.json, cond.npy, Stage 4: Feature Extraction, Stage 3: Joint Annotation (+26 more)

### Community 14 - "names_clean_llm.py"
Cohesion: 0.12
Nodes (15): correct_all(), _hips(), is_empty_entry(), is_non_empty_entry(), main(), add_llm_args(), append_id_list(), LLMClient (+7 more)

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
Cohesion: 0.10
Nodes (14): compute_clip_windows(), get_motion_clip_windows(), _activity_below_threshold(), _discontinuity_above_threshold(), _discontinuity_metrics(), extract_clip_feats(), _format_activity(), _format_discontinuity() (+6 more)

### Community 20 - "gaussian_diffusion.py"
Cohesion: 0.06
Nodes (13): betas_for_alpha_bar(), get_named_beta_schedule(), LossType, ModelMeanType, ModelVarType, mean_flat(), space_timesteps(), create_diffusion() (+5 more)

### Community 21 - "Text Embedding Precomputation"
Cohesion: 0.12
Nodes (14): b64_to_pil(), build_hint_footer(), build_multiview_intro(), build_view_header(), caption_rejection_reason(), gemini_client(), is_retryable_error(), openai_client() (+6 more)

### Community 22 - "names_clean_llm.py"
Cohesion: 0.15
Nodes (10): _alarm_handler(), FatalLLMError, RigTimeout, uninstall_rig_alarm(), build_user_prompt(), clean_rig(), parse_response(), build_correction_prompt() (+2 more)

### Community 23 - "re"
Cohesion: 0.12
Nodes (16): rule_based_clean(), _canon(), clean_japanese_name(), clean_joint_name(), clean_prefixed_name(), clean_spider_name(), clean_standard_name(), extract_side_prefix() (+8 more)

### Community 25 - "render_skeleton_motion_spectral"
Cohesion: 0.13
Nodes (14): _as_xyz(), _capture_rgb(), _cubic_bounds(), _draw_static_skeleton(), _edges_from_parents(), _init_motion_artists(), _new_figure(), render_skeleton_motion() (+6 more)

### Community 26 - "train_diffusion"
Cohesion: 0.05
Nodes (12): Flow Matching, Graph-AdaLN Attention, create_model(), TrainingTracker, _log_metrics(), main(), _resume_from_checkpoint(), _save_checkpoint_and_visualize() (+4 more)

### Community 27 - "torch"
Cohesion: 0.15
Nodes (8): _collect_scalar(), create_padded_matrix(), lengths_to_mask(), mixture_batch_collate(), _pad_joint_axis(), approx_standard_normal_cdf(), discretized_gaussian_log_likelihood(), normal_kl()

### Community 28 - "Motion Feature Extraction"
Cohesion: 0.12
Nodes (9): DatasetConfig, ExperimentConfig, MixamoConfig, ModelConfig, ObjaverseConfig, SamplingArgs, SchedulerConfig, TrainingConfig (+1 more)

### Community 29 - "llm.py"
Cohesion: 0.20
Nodes (4): detect_backend(), generate_local(), generate_openai(), load_local_model()

### Community 30 - "Skeleton Alignment Utilities"
Cohesion: 0.08
Nodes (14): _blank_panel(), first_frame_positions(), _fit_height(), index_motion_npzs(), label_markers(), load_face_pairs(), main(), pair_forward() (+6 more)

### Community 31 - "LLM Client Interface"
Cohesion: 0.12
Nodes (14): model_joint_names(), collect_texts(), encode_texts(), main(), parse_args(), resolve_roots(), cache_path(), load_cache() (+6 more)

### Community 32 - "Sampler"
Cohesion: 0.10
Nodes (3): ode, _fn(), Sampler

### Community 34 - "Blender Rigging Utilities"
Cohesion: 0.11
Nodes (3): UniMateDenoiserBase, UniMateFullAdaLN, UniMateGraphAdaLN

### Community 35 - "pathlib"
Cohesion: 0.08
Nodes (23): Blender Python API (bpy), main(), render_animated_file(), find_pending_stems(), main(), render_glb(), discover_assets(), main() (+15 more)

### Community 36 - "plotting.py"
Cohesion: 0.09
Nodes (11): _draw_caption(), _installed_family(), _mean_advance_pt(), render_skeleton_tpose_ground(), save_skeleton_spectral_grid(), save_skeleton_tpos_spectral(), save_skeleton_tpose(), save_skeleton_tpose_annotated() (+3 more)

### Community 37 - "extract_features.py"
Cohesion: 0.14
Nodes (14): build_object_tasks(), collect_object_npzs(), discover_object_types(), load_clip_trims(), load_filtered_objects(), _object_part_path(), read_root_offsets(), resolve_activity_keep_path() (+6 more)

### Community 38 - "Denoiser Model Variants"
Cohesion: 0.08
Nodes (23): build_user_prompt(), _clean_side(), _format_section(), _hip_fields(), _is_complete(), main(), parse_response(), prefilter_candidates() (+15 more)

### Community 39 - "value_axis"
Cohesion: 0.20
Nodes (5): _log_tick_candidates(), panel_width_in(), pct_axis(), thin_log_ticks(), value_axis()

### Community 40 - "render_action_multiview"
Cohesion: 0.14
Nodes (7): add_camera(), compose_frames_to_video(), enable_color_output(), fit_camera_distance(), remove_camera(), render_action_multiview(), _reset_frames_dir()

### Community 41 - "ODE Sampling Integrators"
Cohesion: 0.19
Nodes (12): main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize(), _threshold_label(), _xlabel() (+4 more)

### Community 42 - "Generative Base Trainer"
Cohesion: 0.12
Nodes (11): align_initial_facing(), align_root_to_ground(), align_root_xz_to_origin(), canonicalize_anim(), get_root_facing_quat(), get_skeleton_diameter(), _normalize(), scale_anim() (+3 more)

### Community 45 - "json"
Cohesion: 0.11
Nodes (11): strip_llm_noise(), load_map(), main(), clean_answer(), load_json(), main(), validate(), load_json() (+3 more)

### Community 46 - "Character Animation Scripts"
Cohesion: 0.13
Nodes (9): add_multi_gpu_args(), is_completed(), merge_shards(), detect_backend(), load_hints(), main(), parse_args(), _caption_prompt() (+1 more)

### Community 48 - "is_canonical_label"
Cohesion: 0.22
Nodes (4): _is_vocab_label(), _warn_non_canonical(), canonical_parts(), is_canonical_label()

### Community 49 - "Mesh Animation Plumbing"
Cohesion: 0.14
Nodes (9): main(), parse_args(), print_table(), summarize(), configure_style(), load_int_map(), parse_int_list(), per_dataset_out_base() (+1 more)

### Community 50 - "Frame Count Visualization"
Cohesion: 0.20
Nodes (9): export_dir(), load_captions(), load_clip(), main(), _render_one(), tile(), _title(), _ground_tiles() (+1 more)

### Community 51 - "load_and_prep_asset"
Cohesion: 0.16
Nodes (8): clear_scene(), find_meshes(), fix_materials(), keep_armature_meshes(), keep_main_mesh_only(), load_and_prep_asset(), set_materials_opaque(), smooth_meshes()

### Community 52 - "math"
Cohesion: 0.23
Nodes (10): accessor(), load_glb(), main(), peak_summary(), quat_angle_deg(), rotation_stats(), vector_stats(), channel() (+2 more)

### Community 57 - "GraphAttnBias"
Cohesion: 0.09
Nodes (5): DiTBlock, FinalLayer, compute_graph_bias(), GraphAttnBias, UniMateGraphCrossAttn

### Community 58 - "Blender Action Management"
Cohesion: 0.20
Nodes (8): _joint_bins(), even_bins(), from_axis(), integer_bins(), kde_grid(), sibling_json_field(), to_axis(), value_range()

### Community 59 - "Plotting Bin Helpers"
Cohesion: 0.21
Nodes (8): ContactJoints, evaluate_clip(), find_ground_contact_joints(), load_cond_dicts(), main(), parse_args(), resolve_object_type(), sweep()

### Community 60 - "os"
Cohesion: 0.09
Nodes (17): _load(), main(), merge_summaries(), _save(), _scan_missing_frame_counts(), collect_keys_from_motions_dir(), default_single_output_path(), find_motion_npz() (+9 more)

### Community 61 - "Metadata I/O"
Cohesion: 0.17
Nodes (3): Logger, _CallerFileFormatter, zero_rank()

### Community 62 - "main"
Cohesion: 0.12
Nodes (9): _error_log_path(), _load_cached_result(), main(), _params_hash(), process_object_task(), _prune_object_clips(), resolve_category_groups(), build_stats() (+1 more)

### Community 63 - "render_tpose_grid"
Cohesion: 0.17
Nodes (6): render_asset_tpose(), build_transformation_mat(), camera_pose_on_sphere(), compose_grid_2x2(), get_scene_armatures(), render_tpose_grid()

### Community 64 - "blender_export.py"
Cohesion: 0.05
Nodes (31): convert_character_to_glb(), convert_fbx_to_glb(), build_vgroup_to_bone_mapping(), children_from_parents(), choose_main_armature(), choose_main_mesh(), collapse_unused_root(), get_all_descendants() (+23 more)

### Community 65 - "auto_label_unirig_quadruped_v2.original.py"
Cohesion: 0.18
Nodes (5): all_paths(), best_non_limb_path(), label_paw_branches(), lowest_path(), split_sides()

### Community 66 - "augmentations.py"
Cohesion: 0.09
Nodes (16): apply_joint_addition_ellipsoid(), apply_joint_addition_linear(), apply_joint_perturbation(), apply_joint_removal(), apply_skeleton_pooling(), bone_length_weighted_sample(), build_children_map(), collapse_single_child_joint() (+8 more)

### Community 67 - "topology_utils.py"
Cohesion: 0.14
Nodes (7): _adjacency_list(), _build_laplacian(), _children_map(), compute_edge_indexs(), compute_laplacian_eigenvectors(), _normalize_eigvecs(), _parse_parents()

### Community 68 - "plot_dataset"
Cohesion: 0.14
Nodes (9): _apply_clip(), plot_comparison(), plot_dataset(), cdf_curve(), crowded_top(), display_name(), kde_proportion(), mark_points() (+1 more)

### Community 69 - "Diffusion Loop Utilities"
Cohesion: 0.31
Nodes (4): compute_directions(), default_output_path(), load_motion_from_npz(), main()

### Community 71 - "argparse"
Cohesion: 0.05
Nodes (37): _action_bone_names(), _adopt_action(), animate_character_fbx(), parse_args(), animate_lbs(), extract_skin(), lbs_deform(), load_motion_local_mats() (+29 more)

### Community 72 - "cougar_nopost"
Cohesion: 0.20
Nodes (10): assets, cougar_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names (+2 more)

### Community 73 - "Train-Eval Splitting"
Cohesion: 0.13
Nodes (4): BERTConditioner, CLIPConditioner, create_text_encoder(), get_text_encoder_dim()

### Community 74 - "Matplotlib Ticker Formatting"
Cohesion: 0.20
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 75 - "save_skeleton_motion"
Cohesion: 0.28
Nodes (5): save_clip(), save_skeleton_motion(), save_skeleton_motion_ground(), save_skeleton_motion_spectral(), _write_video()

### Community 79 - "metadata.py"
Cohesion: 0.19
Nodes (8): load_all_metadata(), load_category_groups(), load_clean_joint_names(), load_face_joint_names(), load_joint_names(), load_json(), load_motion_captions(), print_summary()

### Community 81 - "Diffusion Training Losses"
Cohesion: 0.29
Nodes (4): get_root_objects(), get_scene_bbox(), get_scene_bbox_all_frames(), normalize_scene()

### Community 82 - "goat_nopost"
Cohesion: 0.22
Nodes (9): goat_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names, source (+1 more)

### Community 83 - "Metadata Lookup Helpers"
Cohesion: 0.29
Nodes (7): AgentOps, CONSEJO.md, HANDOFF_LATEST.md, MEMORIA.md, SKILL.md, STATUS.md, WORKFLOW.md

### Community 84 - "hippopotamus_nopost"
Cohesion: 0.22
Nodes (9): hippopotamus_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names, source (+1 more)

### Community 85 - "process_object"
Cohesion: 0.29
Nodes (3): process_object(), resolve_joint_names(), _save_tpose_vis()

### Community 88 - "Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)"
Cohesion: 0.20
Nodes (9): 1. Criterio de Facing y Canonicalización, 2. Criterio de Texturas Embebidas, 3. Criterio de Ciclo Completo (2 Repeticiones), 4. Anclaje de Veredictos Visuales, Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets), Resumen Ejecutivo de Trazabilidad, Rutas de Archivos Verificadas por Asset, Tabla de Trazabilidad de los 28 Assets (+1 more)

### Community 89 - "_build_spectral_encoder"
Cohesion: 0.13
Nodes (3): _build_spectral_encoder(), SignNetSpectralEncoder, WIRESpectralEncoder

### Community 90 - "Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs"
Cohesion: 0.40
Nodes (4): Answer, Outcome, Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs, Source Nodes

### Community 93 - "Cache Digest Utilities"
Cohesion: 0.50
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 94 - "atomic_output_path"
Cohesion: 0.18
Nodes (6): atomic_np_save(), atomic_output_path(), collect_captions(), save_json(), save_metadata_report(), save_outputs()

### Community 96 - "ndarray"
Cohesion: 0.21
Nodes (5): _anchor_for_dir(), _annotate_joints(), _fibonacci_sphere_dirs(), _sample_bone_obstacles(), _smooth_path()

### Community 97 - "cougar_nopost-jump-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_0-0.npy

### Community 113 - "cougar_nopost-jump-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_1-0.npy

### Community 146 - "mean_median_guides"
Cohesion: 0.25
Nodes (4): guide(), legend_loc_clear_of(), mean_median_guides(), x_frac()

### Community 147 - "_capture_rgb"
Cohesion: 0.28
Nodes (5): _box_aspect_from_bounds(), _maybe_rotate_y_up(), render_skeleton_spectral_grid(), render_skeleton_tpose_annotated(), _tight_bounds()

### Community 148 - "cougar_nopost-run-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-run-rep_0-0.npy

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

### Community 163 - "blender_render.py"
Cohesion: 0.16
Nodes (7): clear_normal_maps(), get_expected_clip_dirs(), _gpu_lock_path(), gpu_render_lock(), render_animation(), render_still(), _rendered_marker_path()

### Community 164 - "setup_lighting"
Cohesion: 0.33
Nodes (3): _create_light(), setup_lighting(), _setup_world_environment()

### Community 165 - "samples"
Cohesion: 0.40
Nodes (4): format, motions_dir, runs, samples

### Community 166 - "get_object_metadata"
Cohesion: 0.33
Nodes (3): _dict_get_ci(), get_object_face_joints(), get_object_metadata()

### Community 172 - "Offline cranial-accessory annotation investigation — 2026-11-02"
Cohesion: 0.29
Nodes (6): Final rerun on the same ten GLBs, Finding, Offline cranial-accessory annotation investigation — 2026-11-02, Reuse decision, Scope and safety boundary, Targeted implementation

### Community 173 - "reorder_anim_bfs"
Cohesion: 0.33
Nodes (3): _load_tpos_npz(), bfs_reorder_joints(), reorder_anim_bfs()

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

## Knowledge Gaps
- **24 isolated node(s):** `graphify`, `FFmpeg`, `UniML3D Teaser Diagram`, `Stage 5: Mesh Animation`, `CONSEJO.md` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1329 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **92 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MotionDataset` connect `MotionDataset` to `dataset.py`, `conditioning.py`, `Train-Eval Splitting`, `T5 Text Conditioner`, `._build_text_embeddings`, `._apply_augmentations`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **What connects `graphify`, `FFmpeg`, `UniML3D Teaser Diagram` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `preprocess_char.py` be split into smaller, more focused modules?**
  _Cohesion score 0.04703753957485301 - nodes in this community are weakly interconnected._
- **Why does `process_object()` connect `process_object` to `preprocess_char.py`, `dataset.py`, `extract_features.py`, `topology.py`, `motion_features.py`, `os`, `main`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Should `blender_export.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08754208754208755 - nodes in this community are weakly interconnected._
- **Should `dataset.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08048103607770583 - nodes in this community are weakly interconnected._
- **Should `sample.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06498015873015874 - nodes in this community are weakly interconnected._