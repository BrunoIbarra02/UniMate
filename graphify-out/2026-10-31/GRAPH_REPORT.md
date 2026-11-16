# Graph Report - UniMate  (2026-10-28)

## Corpus Check
- 208 files · ~182,728 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 66 file(s) not represented in the graph (top: .log 56, .fbx 8, (none) 1)

## Summary
- 2385 nodes · 5302 edges · 154 communities (87 shown, 67 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 120 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5d6aabed`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- mesh_animation/common.py
- export_truebones.py
- Summary Merging Tools
- dataset.py
- Blender Export Logic
- Skeleton Augmentations
- blender_export.py
- Asset Export Pipeline
- torch
- Blender Rendering Utilities
- Diffusion Planning Math
- Diffusion Beta Schedules
- Data Processing Documentation
- Denoiser Base Class
- names_correct_llm.py
- Multi-view Character Rendering
- Config Schema Definitions
- Transformer Blocks
- LLM Rig Resolution
- Facing Direction Validation
- VLM Category Classification
- Text Embedding Precomputation
- LLM Joint Selection
- Skeleton Topology Math
- Cross-Attention Layers
- Sampler
- FBX to GLB Conversion
- Motion Feature Extraction
- LLM Face Correction
- Skeleton Alignment Utilities
- LLM Client Interface
- MotionDataset
- SpatioTemporalBlock
- gpu_render_lock
- VLM Data Loading
- Multi-GPU Captioning
- Denoiser Model Variants
- value_axis
- Motion Generation Utilities
- ODE Sampling Integrators
- Generative Base Trainer
- T5 Text Conditioner
- Asset Preprocessing
- json
- Character Animation Scripts
- Joint Distribution Visualization
- Mixture Dataset Loader
- Mesh Animation Plumbing
- Frame Count Visualization
- Motion Dataset Base
- numpy
- recover_unimate_root_quat_and_pos
- trainer.py
- Diffusion Sampling Math
- Task Caching Logic
- caption_rewrite_llm.py
- Blender Action Management
- Plotting Bin Helpers
- os
- Metadata I/O
- T-Pose Visualization
- Image Compositing
- prune_skeleton_shared
- Text Conditioner Base
- DDIM Sampling Logic
- topology_utils.py
- plot_dataset
- Diffusion Loop Utilities
- BERT and CLIP Encoders
- argparse
- animate_fbx.py
- Train-Eval Splitting
- Matplotlib Ticker Formatting
- animate_lbs.py
- render_truebones.py
- save_skeleton_motion
- Export Resume Markers
- export_objaverse.py
- Plot Legend Helpers
- Diffusion Training Losses
- Topology-Specific Loaders
- Metadata Lookup Helpers
- Joint Name Vocabulary
- Animation Dispatcher
- dataset/factory.py
- .__init__
- Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)
- export_general.py
- prepare_skeleton
- Spatio-Temporal Blocks
- _capture_rgb
- Cache Digest Utilities
- Path Labeling
- Timestep Embedding
- ._vb_terms_bpd
- rebuild_action_from_data
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
- export_asset
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
- inbetween_sample_ode
- unique_labels
- compute_graph_bias
- CLAUDE.md
- percentile_stats
- agentops.md

## God Nodes (most connected - your core abstractions)
1. `MotionDataset` - 38 edges
2. `GaussianDiffusion` - 37 edges
3. `MainConfig` - 30 edges
4. `train_diffusion()` - 26 edges
5. `UniMateDenoiserBase` - 24 edges
6. `plot_dataset()` - 23 edges
7. `export_asset()` - 20 edges
8. `plot_comparison()` - 20 edges
9. `plot_dataset()` - 20 edges
10. `create_sample_condition()` - 20 edges

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

## Communities (154 total, 67 thin omitted)

### Community 0 - "mesh_animation/common.py"
Cohesion: 0.17
Nodes (7): animate_character(), build_anims_from_export_npz(), clip_output_path(), drive_and_export(), npz_scalar(), compute_bone_keyframes(), set_scene_timing()

### Community 1 - "export_truebones.py"
Cohesion: 0.14
Nodes (12): Blender Python API (bpy), export_mixamo(), main(), export_species(), extract_single_fbx(), main(), parse_args(), postprocess_and_save() (+4 more)

### Community 2 - "Summary Merging Tools"
Cohesion: 0.05
Nodes (12): Flow Matching, Graph-AdaLN Attention, create_model(), get_text_encoder_dim(), TrainingTracker, _log_metrics(), _resume_from_checkpoint(), _save_checkpoint_and_visualize() (+4 more)

### Community 3 - "dataset.py"
Cohesion: 0.09
Nodes (14): create_sample_condition(), _resolve_dataset(), _validate_motion(), apply_cropping(), apply_normalization(), apply_padding(), build_parent_features(), extract_conditions() (+6 more)

### Community 4 - "Blender Export Logic"
Cohesion: 0.07
Nodes (26): MainConfig, get_joint_names(), parse_keep_joints(), parse_keep_frames(), _encode_prompt(), _gt_valid_lengths(), InferenceArgs, _known_object_types() (+18 more)

### Community 5 - "Skeleton Augmentations"
Cohesion: 0.06
Nodes (34): apply_root_offsets(), load_json(), load_overrides(), load_rig_flags(), main(), needs_side_from_x(), normalize_locomotion(), object_type_of() (+26 more)

### Community 6 - "blender_export.py"
Cohesion: 0.09
Nodes (16): build_skeleton_arrays(), build_vertex_groups_sparse(), build_vgroup_to_bone_mapping(), choose_main_armature(), choose_main_mesh(), compute_bone_weight_sums(), extract_animation_frames(), extract_rest_pose() (+8 more)

### Community 7 - "Asset Export Pipeline"
Cohesion: 0.08
Nodes (18): bake_canonical_asset(), parse_args(), _umeyama(), build_ancestor_map(), delete_dominant_weighted_vertices(), delete_skin_vertices_for_bones(), deselect(), export_selected_to_file() (+10 more)

### Community 8 - "torch"
Cohesion: 0.10
Nodes (11): _collect_scalar(), create_padded_matrix(), lengths_to_mask(), mixture_batch_collate(), _pad_joint_axis(), ClassifierFreeSampleModel, generate_samples(), build_joint_keep_mask() (+3 more)

### Community 9 - "Blender Rendering Utilities"
Cohesion: 0.07
Nodes (4): expand_t_like_x(), GVPCPlan, ICPlan, VPCPlan

### Community 10 - "Diffusion Planning Math"
Cohesion: 0.08
Nodes (21): add_qwen_model_args(), load_json(), load_qwen_model(), qwen_generate(), save_json(), _record(), aggregate_votes(), build_messages() (+13 more)

### Community 11 - "Diffusion Beta Schedules"
Cohesion: 0.08
Nodes (21): correct_all(), _hips(), is_empty_entry(), is_non_empty_entry(), main(), _is_complete(), main(), print_source_summary() (+13 more)

### Community 12 - "Data Processing Documentation"
Cohesion: 0.09
Nodes (5): BaseConditioner, _length_to_mask(), T5Conditioner, TorchAutocast, WhiteSpaceTokenizer

### Community 13 - "Denoiser Base Class"
Cohesion: 0.05
Nodes (34): Quad10 rig release v1, UniML3D Teaser Diagram, Blender, category_groups.json, clean_joint_names.json, cond.npy, Stage 4: Feature Extraction, Stage 3: Joint Annotation (+26 more)

### Community 14 - "names_correct_llm.py"
Cohesion: 0.12
Nodes (13): _alarm_handler(), FatalLLMError, install_rig_alarm(), RigTimeout, uninstall_rig_alarm(), build_user_prompt(), clean_rig(), rule_based_clean() (+5 more)

### Community 15 - "Multi-view Character Rendering"
Cohesion: 0.08
Nodes (17): find_motion_dirs(), find_shard_paths(), frame_mime_type(), is_render_complete(), load_frames_as_base64(), load_multiview_frames(), load_multiview_videos(), render_incomplete_reason() (+9 more)

### Community 16 - "Config Schema Definitions"
Cohesion: 0.08
Nodes (10): DiTBlock, FinalLayer, LlamaRMSNorm, modulate(), RoPEAttention, SwiGLUFFN, SpatioTemporalCrossBlock, TextCrossAttention (+2 more)

### Community 17 - "Transformer Blocks"
Cohesion: 0.07
Nodes (8): _apply_rotary_pos_emb(), _build_spectral_encoder(), GraphRoPE, RopeND, _rotate_half(), SignNetSpectralEncoder, SpectralJointRoPE, WIRESpectralEncoder

### Community 18 - "LLM Rig Resolution"
Cohesion: 0.13
Nodes (13): main(), render_animated_file(), find_pending_stems(), main(), render_glb(), get_expected_clip_dirs(), init_render_engine(), is_asset_render_skipped() (+5 more)

### Community 19 - "Facing Direction Validation"
Cohesion: 0.11
Nodes (13): get_motion_clip_windows(), _activity_below_threshold(), _discontinuity_above_threshold(), _discontinuity_metrics(), extract_clip_feats(), _format_activity(), _format_discontinuity(), load_and_canonicalize_motion() (+5 more)

### Community 20 - "VLM Category Classification"
Cohesion: 0.06
Nodes (3): ode, _fn(), sde

### Community 21 - "Text Embedding Precomputation"
Cohesion: 0.12
Nodes (14): b64_to_pil(), build_hint_footer(), build_multiview_intro(), build_view_header(), caption_rejection_reason(), gemini_client(), is_retryable_error(), openai_client() (+6 more)

### Community 22 - "LLM Joint Selection"
Cohesion: 0.10
Nodes (14): build_topology_cond(), _adjacency_list(), _build_kinchains(), _build_laplacian(), _children_map(), compute_adjacency_matrix(), compute_edge_indexs(), compute_edge_relations_and_distances() (+6 more)

### Community 23 - "Skeleton Topology Math"
Cohesion: 0.09
Nodes (18): _canon(), clean_japanese_name(), clean_joint_name(), clean_prefixed_name(), clean_spider_name(), clean_standard_name(), extract_side_prefix(), _looks_unmapped() (+10 more)

### Community 25 - "Cross-Attention Layers"
Cohesion: 0.16
Nodes (11): _as_xyz(), _cubic_bounds(), _draw_static_skeleton(), _edges_from_parents(), _maybe_rotate_y_up(), _new_figure(), render_skeleton_motion(), render_skeleton_motion_spectral() (+3 more)

### Community 26 - "Sampler"
Cohesion: 0.11
Nodes (4): _build_diffusion(), create_diffusion(), create_transport(), Sampler

### Community 27 - "FBX to GLB Conversion"
Cohesion: 0.08
Nodes (10): betas_for_alpha_bar(), get_named_beta_schedule(), LossType, ModelMeanType, ModelVarType, mean_flat(), ModelType, PathType (+2 more)

### Community 28 - "Motion Feature Extraction"
Cohesion: 0.13
Nodes (9): DatasetConfig, ExperimentConfig, MixamoConfig, ModelConfig, ObjaverseConfig, SamplingArgs, SchedulerConfig, TrainingConfig (+1 more)

### Community 29 - "LLM Face Correction"
Cohesion: 0.11
Nodes (7): UniMateDenoiserBase, build_graph_bias_params(), GraphAttnBias, UniMateFullAdaLN, UniMateFullCrossAttn, UniMateGraphAdaLN, UniMateGraphCrossAttn

### Community 30 - "Skeleton Alignment Utilities"
Cohesion: 0.11
Nodes (13): _blank_panel(), first_frame_positions(), _fit_height(), index_motion_npzs(), label_markers(), load_face_pairs(), main(), pair_forward() (+5 more)

### Community 31 - "LLM Client Interface"
Cohesion: 0.07
Nodes (16): model_joint_names(), create_text_encoder(), collect_texts(), encode_texts(), main(), parse_args(), resolve_roots(), main() (+8 more)

### Community 35 - "gpu_render_lock"
Cohesion: 0.29
Nodes (4): _gpu_lock_path(), gpu_render_lock(), render_animation(), render_still()

### Community 36 - "VLM Data Loading"
Cohesion: 0.09
Nodes (10): _draw_caption(), _ground_tiles(), _installed_family(), _mean_advance_pt(), render_skeleton_tpose_ground(), save_skeleton_spectral_grid(), save_skeleton_tpos_spectral(), save_skeleton_tpose_ground() (+2 more)

### Community 37 - "Multi-GPU Captioning"
Cohesion: 0.14
Nodes (14): build_object_tasks(), collect_object_npzs(), discover_object_types(), load_clip_trims(), load_filtered_objects(), _object_part_path(), read_root_offsets(), resolve_activity_keep_path() (+6 more)

### Community 38 - "Denoiser Model Variants"
Cohesion: 0.11
Nodes (17): build_user_prompt(), _clean_side(), _format_section(), _hip_fields(), parse_response(), prefilter_candidates(), resolve_rig(), _validate_sides() (+9 more)

### Community 39 - "value_axis"
Cohesion: 0.20
Nodes (5): _log_tick_candidates(), panel_width_in(), pct_axis(), thin_log_ticks(), value_axis()

### Community 40 - "Motion Generation Utilities"
Cohesion: 0.12
Nodes (10): discover_assets(), main(), render_asset_tpose(), find_main_fbx(), sanitize_object_type(), add_camera(), compose_grid_2x2(), fit_camera_distance() (+2 more)

### Community 41 - "ODE Sampling Integrators"
Cohesion: 0.19
Nodes (12): main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize(), _threshold_label(), _xlabel() (+4 more)

### Community 42 - "Generative Base Trainer"
Cohesion: 0.13
Nodes (10): align_initial_facing(), align_root_to_ground(), align_root_xz_to_origin(), canonicalize_anim(), get_root_facing_quat(), _normalize(), scale_anim(), scale_by_bone_length() (+2 more)

### Community 44 - "Asset Preprocessing"
Cohesion: 0.12
Nodes (3): _extract_into_tensor(), GaussianDiffusion, get_model_output()

### Community 45 - "json"
Cohesion: 0.11
Nodes (12): load_map(), main(), _load(), main(), merge_summaries(), _save(), _scan_missing_frame_counts(), collect_joint_names_from_markers() (+4 more)

### Community 46 - "Character Animation Scripts"
Cohesion: 0.13
Nodes (9): add_multi_gpu_args(), is_completed(), merge_shards(), detect_backend(), load_hints(), main(), parse_args(), _caption_prompt() (+1 more)

### Community 48 - "Mixture Dataset Loader"
Cohesion: 0.09
Nodes (3): sum_flat(), Transport, noise_ode()

### Community 49 - "Mesh Animation Plumbing"
Cohesion: 0.14
Nodes (9): main(), parse_args(), print_table(), summarize(), configure_style(), load_int_map(), parse_int_list(), per_dataset_out_base() (+1 more)

### Community 50 - "Frame Count Visualization"
Cohesion: 0.23
Nodes (8): export_dir(), load_captions(), load_clip(), main(), _render_one(), tile(), _title(), render_skeleton_motion_ground()

### Community 51 - "Motion Dataset Base"
Cohesion: 0.10
Nodes (14): clear_normal_maps(), clear_scene(), _create_light(), find_meshes(), fix_materials(), keep_armature_meshes(), keep_main_mesh_only(), load_and_prep_asset() (+6 more)

### Community 52 - "numpy"
Cohesion: 0.10
Nodes (15): apply_joint_addition_ellipsoid(), apply_joint_addition_linear(), apply_joint_perturbation(), _augmented_global_positions(), _recompute_all(), recompute_position_features(), recompute_topology_arrays(), recompute_tpos_positions() (+7 more)

### Community 54 - "trainer.py"
Cohesion: 0.08
Nodes (3): _hash_trick(), BaseTrainer, get_logger()

### Community 55 - "Diffusion Sampling Math"
Cohesion: 0.12
Nodes (10): _error_log_path(), _load_cached_result(), main(), _params_hash(), process_object_task(), _prune_object_clips(), resolve_category_groups(), build_stats() (+2 more)

### Community 56 - "Task Caching Logic"
Cohesion: 0.16
Nodes (8): compute_clip_windows(), load_all_metadata(), load_category_groups(), load_clean_joint_names(), load_face_joint_names(), load_joint_names(), load_json(), load_motion_captions()

### Community 57 - "caption_rewrite_llm.py"
Cohesion: 0.19
Nodes (8): generate_local(), generate_openai(), strip_llm_noise(), parse_response(), clean_answer(), load_json(), main(), validate()

### Community 58 - "Blender Action Management"
Cohesion: 0.20
Nodes (8): _joint_bins(), even_bins(), from_axis(), integer_bins(), kde_grid(), sibling_json_field(), to_axis(), value_range()

### Community 59 - "Plotting Bin Helpers"
Cohesion: 0.16
Nodes (10): ContactJoints, evaluate_clip(), find_ground_contact_joints(), load_cond_dicts(), main(), parse_args(), resolve_object_type(), sweep() (+2 more)

### Community 60 - "os"
Cohesion: 0.16
Nodes (7): parse_args(), run_clip_batch(), convert_character_to_glb(), convert_fbx_to_glb(), reset_scene(), parse_batch_args(), run_batch()

### Community 61 - "Metadata I/O"
Cohesion: 0.17
Nodes (3): Logger, _CallerFileFormatter, zero_rank()

### Community 62 - "T-Pose Visualization"
Cohesion: 0.18
Nodes (6): atomic_np_save(), atomic_output_path(), collect_captions(), save_json(), save_metadata_report(), save_outputs()

### Community 63 - "Image Compositing"
Cohesion: 0.19
Nodes (7): collect_keys_from_motions_dir(), default_single_output_path(), find_motion_npz(), load_tpose_from_npz(), main(), render_one(), save_skeleton_tpose_annotated()

### Community 64 - "prune_skeleton_shared"
Cohesion: 0.13
Nodes (11): children_from_parents(), collapse_unused_root(), get_all_descendants(), _compute_mean_bone_len(), _find_deepest_in_chain(), _find_root(), _merge_passthrough_bone(), _pass_merge_passthrough() (+3 more)

### Community 65 - "Text Conditioner Base"
Cohesion: 0.18
Nodes (6): _anchor_for_dir(), _annotate_joints(), _fibonacci_sphere_dirs(), _sample_bone_obstacles(), _smooth_path(), _spectral_to_rgb()

### Community 66 - "DDIM Sampling Logic"
Cohesion: 0.16
Nodes (6): apply_joint_removal(), apply_skeleton_pooling(), bone_length_weighted_sample(), build_children_map(), collapse_single_child_joint(), delete_joint()

### Community 67 - "topology_utils.py"
Cohesion: 0.13
Nodes (7): create_condition(), _adjacency_list(), _build_laplacian(), _children_map(), compute_laplacian_eigenvectors(), _normalize_eigvecs(), _parse_parents()

### Community 68 - "plot_dataset"
Cohesion: 0.14
Nodes (9): _apply_clip(), plot_comparison(), plot_dataset(), cdf_curve(), crowded_top(), display_name(), kde_proportion(), mark_points() (+1 more)

### Community 69 - "Diffusion Loop Utilities"
Cohesion: 0.21
Nodes (6): compute_directions(), default_output_path(), load_motion_from_npz(), main(), _init_motion_artists(), render_skeleton_motion_directed()

### Community 70 - "BERT and CLIP Encoders"
Cohesion: 0.17
Nodes (3): space_timesteps(), SpacedDiffusion, _WrappedModel

### Community 71 - "argparse"
Cohesion: 0.14
Nodes (10): animate_character(), build_anim_from_npy(), build_anim_from_npz(), load_animation(), load_cond_data(), parse_args(), resolve_char_path(), resolve_object_type() (+2 more)

### Community 72 - "animate_fbx.py"
Cohesion: 0.15
Nodes (9): _action_bone_names(), _adopt_action(), animate_character_fbx(), parse_args(), load_character(), export_animated_character(), get_armature_obj(), load_file() (+1 more)

### Community 74 - "Matplotlib Ticker Formatting"
Cohesion: 0.20
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 75 - "animate_lbs.py"
Cohesion: 0.16
Nodes (9): animate_lbs(), extract_skin(), lbs_deform(), load_motion_local_mats(), motion_from_canonical_char(), parse_args(), save_obj_sequence(), parse_blender_argv() (+1 more)

### Community 76 - "render_truebones.py"
Cohesion: 0.14
Nodes (8): main(), render_clip_file(), truebones_clip_name(), compose_frames_to_video(), enable_color_output(), remove_camera(), render_action_multiview(), _reset_frames_dir()

### Community 77 - "save_skeleton_motion"
Cohesion: 0.28
Nodes (5): save_clip(), save_skeleton_motion(), save_skeleton_motion_ground(), save_skeleton_motion_spectral(), _write_video()

### Community 79 - "export_objaverse.py"
Cohesion: 0.16
Nodes (8): main(), parse_args(), list_gltf_files(), load_excluded_stems(), scan_clip_frames(), write_clip_frames_json(), write_export_summary(), write_summary_json()

### Community 81 - "Diffusion Training Losses"
Cohesion: 0.29
Nodes (4): get_root_objects(), get_scene_bbox(), get_scene_bbox_all_frames(), normalize_scene()

### Community 82 - "Topology-Specific Loaders"
Cohesion: 0.14
Nodes (6): DegenerateSkeletonError, _load_tpos_npz(), process_tpose(), bfs_reorder_joints(), get_skeleton_diameter(), reorder_anim_bfs()

### Community 83 - "Metadata Lookup Helpers"
Cohesion: 0.29
Nodes (7): AgentOps, CONSEJO.md, HANDOFF_LATEST.md, MEMORIA.md, SKILL.md, STATUS.md, WORKFLOW.md

### Community 84 - "Joint Name Vocabulary"
Cohesion: 0.29
Nodes (3): process_object(), resolve_joint_names(), _save_tpose_vis()

### Community 85 - "Animation Dispatcher"
Cohesion: 0.33
Nodes (3): _dict_get_ci(), get_object_face_joints(), get_object_metadata()

### Community 86 - "dataset/factory.py"
Cohesion: 0.18
Nodes (3): create_dataset(), create_train_dataloader(), MixtureSampler

### Community 87 - ".__init__"
Cohesion: 0.15
Nodes (3): DiTCrossBlock, InputLayer, TimestepEmbedder

### Community 88 - "Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)"
Cohesion: 0.20
Nodes (9): 1. Criterio de Facing y Canonicalización, 2. Criterio de Texturas Embebidas, 3. Criterio de Ciclo Completo (2 Repeticiones), 4. Anclaje de Veredictos Visuales, Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets), Resumen Ejecutivo de Trazabilidad, Rutas de Archivos Verificadas por Asset, Tabla de Trazabilidad de los 28 Assets (+1 more)

### Community 89 - "export_general.py"
Cohesion: 0.29
Nodes (6): list_asset_files(), main(), parse_args(), pick_importer(), import_fbx(), import_gltf()

### Community 90 - "prepare_skeleton"
Cohesion: 0.20
Nodes (6): _apply_root_rotation(), apply_zup_to_yup(), build_rest_animation(), prepare_skeleton(), prune_secondary_roots(), get_subtree_weight()

### Community 92 - "_capture_rgb"
Cohesion: 0.24
Nodes (5): _box_aspect_from_bounds(), _capture_rgb(), render_skeleton_spectral_grid(), render_skeleton_tpose_annotated(), _tight_bounds()

### Community 93 - "Cache Digest Utilities"
Cohesion: 0.50
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 96 - "._vb_terms_bpd"
Cohesion: 0.24
Nodes (3): approx_standard_normal_cdf(), discretized_gaussian_log_likelihood(), normal_kl()

### Community 97 - "rebuild_action_from_data"
Cohesion: 0.25
Nodes (4): bind_action(), clear_animation_state(), _add_fcurves(), rebuild_action_from_data()

### Community 113 - "export_asset"
Cohesion: 0.15
Nodes (10): export_asset(), export_objaverse(), action_is_relevant_pose(), discover_pose_actions(), remove_tpose_frames(), sanitize_action_name(), unique_clip_names(), _asset_marker_path() (+2 more)

### Community 146 - "mean_median_guides"
Cohesion: 0.25
Nodes (4): guide(), legend_loc_clear_of(), mean_median_guides(), x_frac()

## Knowledge Gaps
- **24 isolated node(s):** `graphify`, `FFmpeg`, `UniML3D Teaser Diagram`, `Stage 5: Mesh Animation`, `CONSEJO.md` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1134 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **67 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MotionDataset` connect `MotionDataset` to `T5 Text Conditioner`, `DDIM Sampling Logic`, `dataset.py`, `LLM Client Interface`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **What connects `graphify`, `FFmpeg`, `UniML3D Teaser Diagram` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `export_truebones.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14 - nodes in this community are weakly interconnected._
- **Why does `process_object()` connect `Joint Name Vocabulary` to `Multi-GPU Captioning`, `Asset Export Pipeline`, `Topology-Specific Loaders`, `Facing Direction Validation`, `numpy`, `Diffusion Sampling Math`, `LLM Joint Selection`, `Skeleton Topology Math`, `os`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Should `Summary Merging Tools` be split into smaller, more focused modules?**
  _Cohesion score 0.045570916538658475 - nodes in this community are weakly interconnected._
- **Should `dataset.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08879492600422834 - nodes in this community are weakly interconnected._
- **Should `Blender Export Logic` be split into smaller, more focused modules?**
  _Cohesion score 0.06892655367231638 - nodes in this community are weakly interconnected._