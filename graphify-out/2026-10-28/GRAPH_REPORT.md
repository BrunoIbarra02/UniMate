# Graph Report - UniMate  (2026-10-28)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 2333 nodes · 5216 edges · 139 communities (70 shown, 69 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 120 edges (avg confidence: 0.9)
- Token cost: 9,865 input · 1,611 output

## Graph Freshness
- Built from commit: `5d6aabed`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Skeleton Plotting Utilities
- Dataset Configuration
- Summary Merging Tools
- Training Infrastructure
- Blender Export Logic
- Skeleton Augmentations
- Sampling Condition Builder
- Asset Export Pipeline
- Full Attention Denoiser
- Blender Rendering Utilities
- Diffusion Planning Math
- Diffusion Beta Schedules
- Data Processing Documentation
- Denoiser Base Class
- Joint Name Cleaning
- Multi-view Character Rendering
- Config Schema Definitions
- Transformer Blocks
- LLM Rig Resolution
- Facing Direction Validation
- VLM Category Classification
- Text Embedding Precomputation
- LLM Joint Selection
- Skeleton Topology Math
- T-Pose Grid Rendering
- Cross-Attention Layers
- SDE Numerical Integrators
- FBX to GLB Conversion
- Motion Feature Extraction
- LLM Face Correction
- Skeleton Alignment Utilities
- LLM Client Interface
- VLM Prompt Construction
- Feature Extraction Tasks
- Blender Rigging Utilities
- Caption Visualization
- VLM Data Loading
- Multi-GPU Captioning
- Denoiser Model Variants
- Data Loading Factories
- Motion Generation Utilities
- ODE Sampling Integrators
- Generative Base Trainer
- T5 Text Conditioner
- Asset Preprocessing
- EMA Model Management
- Character Animation Scripts
- Joint Distribution Visualization
- Mixture Dataset Loader
- Mesh Animation Plumbing
- Frame Count Visualization
- Motion Dataset Base
- Linear Blend Skinning
- Dataset Comparison Plots
- Render Validation Utilities
- Diffusion Sampling Math
- Task Caching Logic
- Metadata Loading
- Blender Action Management
- Plotting Bin Helpers
- Logging Formatter
- Metadata I/O
- T-Pose Visualization
- Image Compositing
- LLM Response Cleaning
- Text Conditioner Base
- Logging and Factories
- Gaussian Diffusion Core
- BERT and CLIP Encoders
- Shell Script Environment
- Matplotlib Ticker Formatting
- Joint Pooling Layers
- Spaced Diffusion Wrapper
- Blender Action Binding
- Export Resume Markers
- Skeleton Video Export
- Plot Legend Helpers
- Metadata Lookup Helpers
- Joint Name Vocabulary
- Animation Dispatcher
- Motion Canonicalization
- BFS Joint Reordering
- Joint Name Embedding
- Motion Input Layer
- Spatio-Temporal Blocks
- GPU Selection Scripts
- Cache Digest Utilities
- Path Labeling
- Timestep Embedding
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
- Motion Editing Script
- Motion Expansion Script
- Motion In-betweening Script
- Text-to-Motion Script
- Model Training Script
- Dataset Overview Diagram
- Motion Editing Diagram
- Motion Expansion Diagram
- Motion In-betweening Diagram
- Qualitative Results Visualization
- Mesh Animation Stage

## God Nodes (most connected - your core abstractions)
1. `unimate.inference.sample` - 74 edges
2. `patch_annotations.py` - 45 edges
3. `MotionDataset` - 38 edges
4. `GaussianDiffusion` - 37 edges
5. `unimate.training.train` - 37 edges
6. `classify_category.py` - 36 edges
7. `MainConfig` - 30 edges
8. `unimate.tools.precompute_text_emb` - 28 edges
9. `train_diffusion()` - 26 edges
10. `UniMateDenoiserBase` - 24 edges

## Surprising Connections (you probably didn't know these)
- `Inference entry point: generate motion samples from a trained model.` --rationale_for--> `unimate.inference.sample`  [EXTRACTED]
  unimate/inference/sample.py → README.md
- `Pre-encode a feature directory's text into an on-disk feature cache. The…` --rationale_for--> `unimate.tools.precompute_text_emb`  [EXTRACTED]
  unimate/tools/precompute_text_emb.py → README.md
- `Train a diffusion model on motions for any skeleton topology. Entry point…` --rationale_for--> `unimate.training.train`  [EXTRACTED]
  unimate/training/train.py → README.md
- `# NOTE: lr_scheduler is NOT wrapped by accelerator. AcceleratedScheduler` --rationale_for--> `unimate.training.train`  [EXTRACTED]
  unimate/training/train.py → README.md
- `Data Process README` --references--> `UniML3D Teaser Diagram`  [EXTRACTED]
  data_process/README.md → assets/teaser.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Data Processing Pipeline** — stage_1_export, stage_2_caption_category, stage_3_joint_annotation, stage_4_extract, stage_5_animate [EXTRACTED 1.00]
- **UniMate Core Execution Flow** — unimate_training_train, unimate_inference_sample, unimate_tools_precompute_text_emb [EXTRACTED 1.00]
- **UniML3D Data Processing Pipeline** — data_process_motion_export, data_process_motion_rendering, data_process_vlm_caption, data_process_joint_annotation, data_process_feature_extraction, data_process_mesh_animation [EXTRACTED 1.00]
- **Zero-Shot Motion Applications** — unimate_inference_sample, flow_matching [INFERRED 0.85]
- **Motion Generation and Editing Tasks** — assets_motion_editing, assets_motion_expansion, assets_motion_in_betweening [INFERRED 0.90]

## Communities (139 total, 69 thin omitted)

### Community 0 - "Skeleton Plotting Utilities"
Cohesion: 0.06
Nodes (35): _anchor_for_dir(), _annotate_joints(), _as_xyz(), _box_aspect_from_bounds(), _capture_rgb(), _cubic_bounds(), _draw_caption(), _draw_static_skeleton() (+27 more)

### Community 1 - "Dataset Configuration"
Cohesion: 0.05
Nodes (33): MainConfig, create_dataset(), build_joint_keep_mask(), get_joint_names(), parse_keep_joints(), build_keep_mask(), parse_keep_frames(), unimate.inference.sample (+25 more)

### Community 2 - "Summary Merging Tools"
Cohesion: 0.05
Nodes (41): merge_summaries.py, _load(), main(), merge_summaries(), _save(), _scan_missing_frame_counts(), patch_annotations.py, apply_root_offsets() (+33 more)

### Community 3 - "Training Infrastructure"
Cohesion: 0.04
Nodes (15): run_download.sh, run_download.sh script, Flow Matching, Graph-AdaLN Attention, TrainingTracker, unimate.training.train, _log_metrics(), main() (+7 more)

### Community 4 - "Blender Export Logic"
Cohesion: 0.04
Nodes (36): action_is_relevant_pose(), _apply_root_rotation(), apply_zup_to_yup(), build_rest_animation(), build_skeleton_arrays(), build_vertex_groups_sparse(), build_vgroup_to_bone_mapping(), children_from_parents() (+28 more)

### Community 5 - "Skeleton Augmentations"
Cohesion: 0.06
Nodes (26): apply_joint_addition_ellipsoid(), apply_joint_addition_linear(), apply_joint_perturbation(), apply_joint_removal(), apply_skeleton_pooling(), _augmented_global_positions(), bone_length_weighted_sample(), build_children_map() (+18 more)

### Community 6 - "Sampling Condition Builder"
Cohesion: 0.07
Nodes (20): create_sample_condition(), _resolve_dataset(), _validate_motion(), apply_cropping(), apply_normalization(), apply_padding(), build_parent_features(), extract_conditions() (+12 more)

### Community 7 - "Asset Export Pipeline"
Cohesion: 0.09
Nodes (26): export_asset(), list_asset_files(), main(), parse_args(), pick_importer(), export_objaverse(), main(), parse_args() (+18 more)

### Community 8 - "Full Attention Denoiser"
Cohesion: 0.06
Nodes (9): UniMateFullAdaLN, _apply_rotary_pos_emb(), _build_spectral_encoder(), GraphRoPE, RopeND, _rotate_half(), SignNetSpectralEncoder, SpectralJointRoPE (+1 more)

### Community 9 - "Blender Rendering Utilities"
Cohesion: 0.06
Nodes (25): clear_normal_maps(), clear_scene(), compose_frames_to_video(), _create_light(), enable_color_output(), find_meshes(), fix_materials(), get_root_objects() (+17 more)

### Community 10 - "Diffusion Planning Math"
Cohesion: 0.06
Nodes (5): expand_t_like_x(), GVPCPlan, ICPlan, VPCPlan, noise_ode()

### Community 11 - "Diffusion Beta Schedules"
Cohesion: 0.07
Nodes (12): betas_for_alpha_bar(), get_named_beta_schedule(), LossType, ModelMeanType, ModelVarType, approx_standard_normal_cdf(), discretized_gaussian_log_likelihood(), normal_kl() (+4 more)

### Community 12 - "Data Processing Documentation"
Cohesion: 0.06
Nodes (40): UniML3D Teaser Diagram, Blender, category_groups.json, clean_joint_names.json, cond.npy, Stage 4: Feature Extraction, Stage 3: Joint Annotation, Stage 1: Motion Export (+32 more)

### Community 13 - "Denoiser Base Class"
Cohesion: 0.08
Nodes (4): UniMateDenoiserBase, DiTCrossBlock, UniMateGraphAdaLN, UniMateGraphCrossAttn

### Community 14 - "Joint Name Cleaning"
Cohesion: 0.09
Nodes (18): _canon(), clean_japanese_name(), clean_joint_name(), clean_prefixed_name(), clean_spider_name(), clean_standard_name(), extract_side_prefix(), _looks_unmapped() (+10 more)

### Community 15 - "Multi-view Character Rendering"
Cohesion: 0.11
Nodes (18): main(), render_animated_file(), find_pending_stems(), main(), render_glb(), main(), render_clip_file(), discover_pose_actions() (+10 more)

### Community 16 - "Config Schema Definitions"
Cohesion: 0.10
Nodes (9): DatasetConfig, ExperimentConfig, MixamoConfig, ModelConfig, ObjaverseConfig, SamplingArgs, SchedulerConfig, TrainingConfig (+1 more)

### Community 17 - "Transformer Blocks"
Cohesion: 0.10
Nodes (8): DiTBlock, LlamaRMSNorm, RoPEAttention, SwiGLUFFN, SpatioTemporalCrossBlock, TextCrossAttention, SpatialGraphSelfAttention, TemporalSelfAttention

### Community 18 - "LLM Rig Resolution"
Cohesion: 0.12
Nodes (15): resolve_rig(), _alarm_handler(), FatalLLMError, install_rig_alarm(), RigTimeout, uninstall_rig_alarm(), build_user_prompt(), clean_rig() (+7 more)

### Community 19 - "Facing Direction Validation"
Cohesion: 0.10
Nodes (14): _blank_panel(), first_frame_positions(), _fit_height(), index_motion_npzs(), label_markers(), load_face_pairs(), main(), pair_forward() (+6 more)

### Community 20 - "VLM Category Classification"
Cohesion: 0.10
Nodes (18): add_qwen_model_args(), load_qwen_model(), qwen_generate(), save_json(), classify_category.py, aggregate_votes(), build_messages(), classify_asset() (+10 more)

### Community 21 - "Text Embedding Precomputation"
Cohesion: 0.11
Nodes (15): model_joint_names(), create_text_encoder(), unimate.tools.precompute_text_emb, collect_texts(), encode_texts(), main(), parse_args(), resolve_roots() (+7 more)

### Community 22 - "LLM Joint Selection"
Cohesion: 0.11
Nodes (16): build_user_prompt(), _clean_side(), _format_section(), _hip_fields(), parse_response(), prefilter_candidates(), _validate_sides(), _digit_runs() (+8 more)

### Community 23 - "Skeleton Topology Math"
Cohesion: 0.10
Nodes (13): _adjacency_list(), _build_kinchains(), _build_laplacian(), _children_map(), compute_adjacency_matrix(), compute_edge_indexs(), compute_edge_relations_and_distances(), compute_joint_depths() (+5 more)

### Community 24 - "T-Pose Grid Rendering"
Cohesion: 0.09
Nodes (13): discover_assets(), main(), render_asset_tpose(), find_main_fbx(), sanitize_object_type(), add_camera(), build_transformation_mat(), camera_pose_on_sphere() (+5 more)

### Community 25 - "Cross-Attention Layers"
Cohesion: 0.13
Nodes (5): FinalLayer, modulate(), build_graph_bias_params(), compute_graph_bias(), GraphAttnBias

### Community 27 - "FBX to GLB Conversion"
Cohesion: 0.14
Nodes (10): Blender Python API (bpy), export_mixamo(), main(), convert_character_to_glb(), convert_fbx_to_glb(), import_fbx(), reset_scene(), parse_batch_args() (+2 more)

### Community 28 - "Motion Feature Extraction"
Cohesion: 0.10
Nodes (13): compute_clip_windows(), get_motion_clip_windows(), _activity_below_threshold(), _discontinuity_above_threshold(), _discontinuity_metrics(), extract_clip_feats(), _format_activity(), _format_discontinuity() (+5 more)

### Community 29 - "LLM Face Correction"
Cohesion: 0.13
Nodes (13): correct_all(), _hips(), is_empty_entry(), is_non_empty_entry(), main(), _is_complete(), resolve_all(), append_id_list() (+5 more)

### Community 30 - "Skeleton Alignment Utilities"
Cohesion: 0.12
Nodes (11): align_initial_facing(), align_root_to_ground(), align_root_xz_to_origin(), canonicalize_anim(), get_root_facing_quat(), get_skeleton_diameter(), _normalize(), scale_anim() (+3 more)

### Community 31 - "LLM Client Interface"
Cohesion: 0.11
Nodes (11): main(), print_source_summary(), add_llm_args(), detect_backend(), generate_local(), generate_openai(), LLMClient, load_local_model() (+3 more)

### Community 32 - "VLM Prompt Construction"
Cohesion: 0.15
Nodes (11): b64_to_pil(), build_hint_footer(), build_multiview_intro(), build_view_header(), gemini_client(), is_retryable_error(), _build_openai_messages(), _build_qwen_messages() (+3 more)

### Community 33 - "Feature Extraction Tasks"
Cohesion: 0.14
Nodes (14): build_object_tasks(), collect_object_npzs(), discover_object_types(), load_clip_trims(), load_filtered_objects(), _object_part_path(), read_root_offsets(), resolve_activity_keep_path() (+6 more)

### Community 34 - "Blender Rigging Utilities"
Cohesion: 0.13
Nodes (10): build_ancestor_map(), delete_dominant_weighted_vertices(), delete_skin_vertices_for_bones(), find_skinned_meshes(), _find_upstream_image_node(), merge_extra_bone_weights(), remove_armature_bones(), simplify_materials_for_fbx() (+2 more)

### Community 35 - "Caption Visualization"
Cohesion: 0.15
Nodes (11): export_dir(), load_captions(), load_clip(), main(), _render_one(), tile(), _title(), compute_directions() (+3 more)

### Community 36 - "VLM Data Loading"
Cohesion: 0.09
Nodes (9): find_motion_dirs(), find_shard_paths(), frame_mime_type(), is_render_complete(), load_frames_as_base64(), openai_client(), select_frame_paths(), shard_output_path() (+1 more)

### Community 37 - "Multi-GPU Captioning"
Cohesion: 0.12
Nodes (10): add_multi_gpu_args(), is_completed(), merge_shards(), detect_backend(), image_params(), load_hints(), main(), parse_args() (+2 more)

### Community 38 - "Denoiser Model Variants"
Cohesion: 0.10
Nodes (5): UniMateFullCrossAttn, space_timesteps(), ModelType, PathType, WeightType

### Community 39 - "Data Loading Factories"
Cohesion: 0.11
Nodes (7): create_train_dataloader(), _collect_scalar(), create_padded_matrix(), lengths_to_mask(), mixture_batch_collate(), _pad_joint_axis(), MixtureSampler

### Community 40 - "Motion Generation Utilities"
Cohesion: 0.13
Nodes (6): ClassifierFreeSampleModel, generate_samples(), build_overlap_keep_mask(), expand_motion_chain(), seed_expansion_x1(), inbetween_sample_ode()

### Community 41 - "ODE Sampling Integrators"
Cohesion: 0.10
Nodes (3): ode, _fn(), Sampler

### Community 43 - "T5 Text Conditioner"
Cohesion: 0.12
Nodes (4): _hash_trick(), _length_to_mask(), T5Conditioner, WhiteSpaceTokenizer

### Community 44 - "Asset Preprocessing"
Cohesion: 0.12
Nodes (9): quat_pos_to_mats(), bake_canonical_asset(), parse_args(), _umeyama(), deselect(), export_selected_to_file(), select_objs(), update_scene() (+1 more)

### Community 46 - "Character Animation Scripts"
Cohesion: 0.16
Nodes (9): parse_args(), parse_args(), parse_args(), resolve_char_path(), resolve_object_type(), parse_args(), parse_blender_argv(), run_clip_batch() (+1 more)

### Community 47 - "Joint Distribution Visualization"
Cohesion: 0.12
Nodes (10): main(), parse_args(), print_table(), summarize(), configure_style(), load_int_map(), parse_int_list(), per_dataset_out_base() (+2 more)

### Community 49 - "Mesh Animation Plumbing"
Cohesion: 0.17
Nodes (7): animate_character(), build_anims_from_export_npz(), clip_output_path(), drive_and_export(), npz_scalar(), compute_bone_keyframes(), set_scene_timing()

### Community 50 - "Frame Count Visualization"
Cohesion: 0.19
Nodes (12): main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize(), _threshold_label(), _xlabel() (+4 more)

### Community 52 - "Linear Blend Skinning"
Cohesion: 0.16
Nodes (9): animate_lbs(), extract_skin(), lbs_deform(), load_motion_local_mats(), motion_from_canonical_char(), parse_args(), save_obj_sequence(), build_anim_from_npz() (+1 more)

### Community 53 - "Dataset Comparison Plots"
Cohesion: 0.14
Nodes (9): _apply_clip(), plot_comparison(), plot_dataset(), cdf_curve(), crowded_top(), display_name(), kde_proportion(), mark_points() (+1 more)

### Community 54 - "Render Validation Utilities"
Cohesion: 0.16
Nodes (10): caption_rejection_reason(), load_multiview_frames(), load_multiview_videos(), render_incomplete_reason(), uniform_subsample(), _view_label_from_id(), generate_openai(), generate_qwen() (+2 more)

### Community 56 - "Task Caching Logic"
Cohesion: 0.13
Nodes (9): _error_log_path(), _load_cached_result(), main(), _params_hash(), process_object_task(), _prune_object_clips(), build_stats(), check_metadata_object_types_consistent() (+1 more)

### Community 57 - "Metadata Loading"
Cohesion: 0.16
Nodes (8): resolve_category_groups(), load_all_metadata(), load_category_groups(), load_clean_joint_names(), load_face_joint_names(), load_joint_names(), load_json(), load_motion_captions()

### Community 58 - "Blender Action Management"
Cohesion: 0.14
Nodes (8): _action_bone_names(), _adopt_action(), animate_character_fbx(), load_character(), export_animated_character(), get_armature_obj(), load_file(), repair_and_pack_textures()

### Community 59 - "Plotting Bin Helpers"
Cohesion: 0.18
Nodes (8): _joint_bins(), even_bins(), from_axis(), integer_bins(), kde_grid(), sibling_json_field(), to_axis(), value_range()

### Community 60 - "Logging Formatter"
Cohesion: 0.17
Nodes (3): Logger, _CallerFileFormatter, zero_rank()

### Community 61 - "Metadata I/O"
Cohesion: 0.19
Nodes (6): atomic_np_save(), atomic_output_path(), collect_captions(), save_json(), save_metadata_report(), save_outputs()

### Community 62 - "T-Pose Visualization"
Cohesion: 0.19
Nodes (7): collect_keys_from_motions_dir(), default_single_output_path(), find_motion_npz(), load_tpose_from_npz(), main(), render_one(), save_skeleton_tpose_annotated()

### Community 63 - "Image Compositing"
Cohesion: 0.14
Nodes (5): flatten_rgba(), load_json(), _record(), ExportEvidence, _has_word()

### Community 64 - "LLM Response Cleaning"
Cohesion: 0.24
Nodes (8): strip_llm_noise(), load_map(), main(), caption_rewrite_llm.py, clean_answer(), load_json(), main(), validate()

### Community 71 - "Shell Script Environment"
Cohesion: 0.20
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 74 - "Matplotlib Ticker Formatting"
Cohesion: 0.20
Nodes (5): _log_tick_candidates(), panel_width_in(), pct_axis(), thin_log_ticks(), value_axis()

### Community 77 - "Blender Action Binding"
Cohesion: 0.25
Nodes (4): bind_action(), clear_animation_state(), _add_fcurves(), rebuild_action_from_data()

### Community 78 - "Export Resume Markers"
Cohesion: 0.28
Nodes (4): _asset_marker_path(), collect_joint_names_from_markers(), is_asset_complete(), merge_joint_names()

### Community 79 - "Skeleton Video Export"
Cohesion: 0.28
Nodes (5): save_clip(), save_skeleton_motion(), save_skeleton_motion_ground(), save_skeleton_motion_spectral(), _write_video()

### Community 80 - "Plot Legend Helpers"
Cohesion: 0.25
Nodes (4): guide(), legend_loc_clear_of(), mean_median_guides(), x_frac()

### Community 83 - "Metadata Lookup Helpers"
Cohesion: 0.33
Nodes (3): _dict_get_ci(), get_object_face_joints(), get_object_metadata()

### Community 85 - "Animation Dispatcher"
Cohesion: 0.33
Nodes (3): animate_character(), build_anim_from_npy(), load_animation()

### Community 86 - "Motion Canonicalization"
Cohesion: 0.33
Nodes (3): load_and_canonicalize_motion(), _load_npz_anim(), _names_permutation()

### Community 87 - "BFS Joint Reordering"
Cohesion: 0.33
Nodes (3): _load_tpos_npz(), bfs_reorder_joints(), reorder_anim_bfs()

### Community 92 - "GPU Selection Scripts"
Cohesion: 0.50
Nodes (3): handle_help(), print_usage(), _common.sh script

## Knowledge Gaps
- **17 isolated node(s):** `Flow Matching`, `Graph-AdaLN Attention`, `Motion Library`, `Codex AgentOps Skill`, `Dataset Overview Diagram` (+12 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1101 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `unimate.inference.sample` connect `Dataset Configuration` to `Summary Merging Tools`, `Training Infrastructure`, `Skeleton Augmentations`, `Sampling Condition Builder`, `Asset Export Pipeline`, `Diffusion Beta Schedules`, `Joint Name Cleaning`, `Config Schema Definitions`, `LLM Rig Resolution`, `Text Embedding Precomputation`, `Cross-Attention Layers`, `Denoiser Model Variants`, `Data Loading Factories`, `Motion Generation Utilities`, `ODE Sampling Integrators`, `Generative Base Trainer`, `T5 Text Conditioner`, `EMA Model Management`, `LLM Response Cleaning`, `Logging and Factories`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **What connects `Flow Matching`, `Graph-AdaLN Attention`, `Motion Library` to the rest of the system?**
  _17 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Skeleton Plotting Utilities` be split into smaller, more focused modules?**
  _Cohesion score 0.06127206127206127 - nodes in this community are weakly interconnected._
- **Why does `unimate.training.train` connect `Training Infrastructure` to `Dataset Configuration`, `Logging and Factories`, `Denoiser Model Variants`, `Data Loading Factories`, `Asset Export Pipeline`, `Diffusion Beta Schedules`, `T5 Text Conditioner`, `Config Schema Definitions`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Should `Dataset Configuration` be split into smaller, more focused modules?**
  _Cohesion score 0.05160628844839371 - nodes in this community are weakly interconnected._
- **Why does `classify_category.py` connect `VLM Category Classification` to `LLM Response Cleaning`, `Summary Merging Tools`, `VLM Data Loading`, `Multi-GPU Captioning`, `Skeleton Augmentations`, `Asset Export Pipeline`, `Data Processing Documentation`, `Character Animation Scripts`, `Joint Name Cleaning`, `LLM Rig Resolution`, `FBX to GLB Conversion`, `Image Compositing`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Should `Summary Merging Tools` be split into smaller, more focused modules?**
  _Cohesion score 0.053830227743271224 - nodes in this community are weakly interconnected._