# Graph Report - UniMate  (2026-11-03)

## Corpus Check
- 445 files · ~288,142 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 265 file(s) not represented in the graph (top: .log 248, .fbx 8, .tsv 7)

## Summary
- 2700 nodes · 5683 edges · 186 communities (101 shown, 85 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 122 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `021b8ceb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- preprocess_char.py
- sys
- numpy
- dataset.py
- sample.py
- patch_annotations.py
- sample.py
- topology.py
- compute_laplacian_eigenvectors
- ICPlan
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
- torch
- Text Embedding Precomputation
- normalize_scene
- re
- load_and_canonicalize_motion
- render_skeleton_motion_spectral
- train_diffusion
- dataset/factory.py
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
- dist_plot.py
- _UnconditionalWrapper
- ODE Sampling Integrators
- Generative Base Trainer
- T5 Text Conditioner
- _extract_into_tensor
- json
- Character Animation Scripts
- Joint Distribution Visualization
- detect_backend
- Frame Count Visualization
- blender_render.py
- math
- .__init__
- gaussian_diffusion.py
- load_and_prep_asset
- GraphAttnBias
- Plotting Bin Helpers
- os
- Metadata I/O
- main
- blender_export.py
- auto_label_unirig_quadruped_v2.original.py
- apply_skeleton_pooling
- plot_dataset
- Diffusion Loop Utilities
- BERT and CLIP Encoders
- argparse
- cougar_nopost
- _build_spectral_encoder
- Matplotlib Ticker Formatting
- vis_tpose.py
- Export Resume Markers
- metadata.py
- goat_nopost
- Metadata Lookup Helpers
- hippopotamus_nopost
- render_mixamo.py
- render_tpose.py
- InputLayer
- Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)
- BERTConditioner
- Q: Investigate safe cranial-accessory vocabulary for the ten existing rig-wave GLBs
- MotionDataset
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
- os
- cougar_nopost-run-rep_0-0.npy
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
- save_skeleton_motion
- samples
- get_object_metadata
- run_canary_4s.sh
- continue_canary_4s.sh
- probe_results.sh
- rerender_24fps.sh
- Offline cranial-accessory annotation investigation — 2026-11-02
- reorder_anim_bfs
- horse_nopost catalogue-verb feasibility test — 2026-11-02
- Q: How should the quad10 production canary use motion expansion, frozen rigs, and existing QA?
- run_initial_wave.sh
- deer_nopost full-action feasibility test — 2026-11-02
- setup_lighting
- ._build_text_embeddings
- SpatioTemporalBlock
- run_rig_wave_profiles.sh
- _cache_params
- run_offline_eval.sh
- run_hippo_wallow_fallback.sh
- prepare_rig_wave.sh
- run_walk_variants.sh
- 2026-11-02 21:55 +03:00 — dramatic catalogue wave started
- anim_wave_20261102_deer_catalogue_runner.sh
- anim_wave_20261102_horse_catalogue_runner.sh
- load_armature
- TimestepEmbedder
- GaussianDiffusion

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

## Communities (186 total, 85 thin omitted)

### Community 0 - "preprocess_char.py"
Cohesion: 0.04
Nodes (42): animate_lbs(), extract_skin(), lbs_deform(), load_motion_local_mats(), motion_from_canonical_char(), save_obj_sequence(), animate_character(), build_anim_from_npy() (+34 more)

### Community 1 - "sys"
Cohesion: 0.08
Nodes (29): Blender Python API (bpy), export_asset(), list_asset_files(), main(), parse_args(), pick_importer(), export_mixamo(), main() (+21 more)

### Community 2 - "numpy"
Cohesion: 0.06
Nodes (24): apply_joint_addition_ellipsoid(), apply_joint_addition_linear(), apply_joint_perturbation(), _augmented_global_positions(), delete_joint(), _recompute_all(), recompute_position_features(), recompute_topology_arrays() (+16 more)

### Community 3 - "dataset.py"
Cohesion: 0.06
Nodes (21): create_sample_condition(), _resolve_dataset(), _collect_scalar(), create_padded_matrix(), lengths_to_mask(), mixture_batch_collate(), _pad_joint_axis(), create_condition() (+13 more)

### Community 4 - "sample.py"
Cohesion: 0.08
Nodes (22): MainConfig, parse_keep_joints(), parse_keep_frames(), _encode_prompt(), _gt_valid_lengths(), InferenceArgs, _known_object_types(), _load_expand_test_cases() (+14 more)

### Community 5 - "patch_annotations.py"
Cohesion: 0.06
Nodes (34): apply_root_offsets(), load_json(), load_overrides(), load_rig_flags(), main(), needs_side_from_x(), normalize_locomotion(), object_type_of() (+26 more)

### Community 6 - "sample.py"
Cohesion: 0.07
Nodes (6): Flow Matching, Graph-AdaLN Attention, get_joint_names(), create_model(), get_text_encoder_dim(), get_logger()

### Community 7 - "topology.py"
Cohesion: 0.15
Nodes (7): _adjacency_list(), _build_kinchains(), _children_map(), compute_edge_relations_and_distances(), compute_joint_depths(), compute_kinematic_chains(), _reverse_insort()

### Community 8 - "compute_laplacian_eigenvectors"
Cohesion: 0.18
Nodes (6): _build_laplacian(), compute_adjacency_matrix(), compute_edge_indexs(), compute_laplacian_eigenvectors(), _normalize_eigvecs(), _parse_parents()

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
Cohesion: 0.08
Nodes (6): BaseConditioner, _hash_trick(), _length_to_mask(), T5Conditioner, TorchAutocast, WhiteSpaceTokenizer

### Community 13 - "Denoiser Base Class"
Cohesion: 0.05
Nodes (34): Quad10 rig release v1, UniML3D Teaser Diagram, Blender, category_groups.json, clean_joint_names.json, cond.npy, Stage 4: Feature Extraction, Stage 3: Joint Annotation (+26 more)

### Community 14 - "names_clean_llm.py"
Cohesion: 0.10
Nodes (19): correct_all(), _hips(), is_empty_entry(), is_non_empty_entry(), main(), add_llm_args(), _alarm_handler(), append_id_list() (+11 more)

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
Cohesion: 0.12
Nodes (12): compute_clip_windows(), get_motion_clip_windows(), _activity_below_threshold(), _discontinuity_above_threshold(), _discontinuity_metrics(), extract_clip_feats(), _format_activity(), _format_discontinuity() (+4 more)

### Community 20 - "torch"
Cohesion: 0.08
Nodes (11): ClassifierFreeSampleModel, generate_samples(), build_joint_keep_mask(), build_overlap_keep_mask(), expand_motion_chain(), seed_expansion_x1(), build_keep_mask(), inbetween_sample_ode() (+3 more)

### Community 21 - "Text Embedding Precomputation"
Cohesion: 0.12
Nodes (14): b64_to_pil(), build_hint_footer(), build_multiview_intro(), build_view_header(), caption_rejection_reason(), gemini_client(), is_retryable_error(), openai_client() (+6 more)

### Community 22 - "normalize_scene"
Cohesion: 0.29
Nodes (4): get_root_objects(), get_scene_bbox(), get_scene_bbox_all_frames(), normalize_scene()

### Community 23 - "re"
Cohesion: 0.08
Nodes (22): build_user_prompt(), clean_all(), clean_rig(), main(), parse_response(), rule_based_clean(), _canon(), clean_japanese_name() (+14 more)

### Community 24 - "load_and_canonicalize_motion"
Cohesion: 0.33
Nodes (3): load_and_canonicalize_motion(), _load_npz_anim(), _names_permutation()

### Community 25 - "render_skeleton_motion_spectral"
Cohesion: 0.13
Nodes (13): _as_xyz(), _capture_rgb(), _cubic_bounds(), _draw_caption(), _draw_static_skeleton(), _init_motion_artists(), _maybe_rotate_y_up(), _new_figure() (+5 more)

### Community 26 - "train_diffusion"
Cohesion: 0.05
Nodes (9): TrainingTracker, _log_metrics(), main(), _resume_from_checkpoint(), _save_checkpoint_and_visualize(), _set_sampler_epoch(), train_diffusion(), TrainingArgs (+1 more)

### Community 27 - "dataset/factory.py"
Cohesion: 0.18
Nodes (3): create_dataset(), create_train_dataloader(), MixtureSampler

### Community 28 - "Motion Feature Extraction"
Cohesion: 0.11
Nodes (9): DatasetConfig, ExperimentConfig, MixamoConfig, ModelConfig, ObjaverseConfig, SamplingArgs, SchedulerConfig, TrainingConfig (+1 more)

### Community 29 - "llm.py"
Cohesion: 0.13
Nodes (9): FatalLLMError, generate_local(), generate_openai(), LLMClient, strip_llm_noise(), clean_answer(), load_json(), main() (+1 more)

### Community 30 - "Skeleton Alignment Utilities"
Cohesion: 0.10
Nodes (14): _blank_panel(), first_frame_positions(), _fit_height(), index_motion_npzs(), label_markers(), load_face_pairs(), main(), pair_forward() (+6 more)

### Community 31 - "LLM Client Interface"
Cohesion: 0.12
Nodes (14): create_text_encoder(), collect_texts(), encode_texts(), main(), parse_args(), resolve_roots(), cache_path(), load_cache() (+6 more)

### Community 32 - "Sampler"
Cohesion: 0.06
Nodes (3): ode, _fn(), sde

### Community 34 - "Blender Rigging Utilities"
Cohesion: 0.11
Nodes (3): UniMateDenoiserBase, UniMateFullAdaLN, UniMateGraphAdaLN

### Community 35 - "pathlib"
Cohesion: 0.11
Nodes (15): find_pending_stems(), main(), render_glb(), main(), render_clip_file(), action_is_relevant_pose(), discover_pose_actions(), truebones_clip_name() (+7 more)

### Community 36 - "plotting.py"
Cohesion: 0.10
Nodes (9): _ground_tiles(), _installed_family(), _mean_advance_pt(), render_skeleton_tpose_ground(), save_skeleton_spectral_grid(), save_skeleton_tpos_spectral(), save_skeleton_tpose_ground(), _wrap_title() (+1 more)

### Community 37 - "extract_features.py"
Cohesion: 0.14
Nodes (14): build_object_tasks(), collect_object_npzs(), discover_object_types(), load_clip_trims(), load_filtered_objects(), _object_part_path(), read_root_offsets(), resolve_activity_keep_path() (+6 more)

### Community 38 - "Denoiser Model Variants"
Cohesion: 0.08
Nodes (23): build_user_prompt(), _clean_side(), _format_section(), _hip_fields(), _is_complete(), main(), parse_response(), prefilter_candidates() (+15 more)

### Community 39 - "dist_plot.py"
Cohesion: 0.06
Nodes (19): configure_style(), guide(), integer_bins(), label_for(), legend_loc_clear_of(), load_int_map(), _log_tick_candidates(), mark_points() (+11 more)

### Community 41 - "ODE Sampling Integrators"
Cohesion: 0.15
Nodes (15): main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize(), _threshold_label(), _xlabel() (+7 more)

### Community 42 - "Generative Base Trainer"
Cohesion: 0.12
Nodes (11): align_initial_facing(), align_root_to_ground(), align_root_xz_to_origin(), canonicalize_anim(), get_root_facing_quat(), get_skeleton_diameter(), _normalize(), scale_anim() (+3 more)

### Community 45 - "json"
Cohesion: 0.09
Nodes (10): load_map(), main(), load_json(), main(), main(), sha256(), generate_matrix(), descendants() (+2 more)

### Community 46 - "Character Animation Scripts"
Cohesion: 0.13
Nodes (9): add_multi_gpu_args(), is_completed(), merge_shards(), detect_backend(), load_hints(), main(), parse_args(), _caption_prompt() (+1 more)

### Community 50 - "Frame Count Visualization"
Cohesion: 0.23
Nodes (8): export_dir(), load_captions(), load_clip(), main(), _render_one(), tile(), _title(), render_skeleton_motion_ground()

### Community 51 - "blender_render.py"
Cohesion: 0.10
Nodes (12): add_camera(), build_transformation_mat(), camera_pose_on_sphere(), compose_grid_2x2(), fit_camera_distance(), get_scene_armatures(), _gpu_lock_path(), gpu_render_lock() (+4 more)

### Community 52 - "math"
Cohesion: 0.23
Nodes (10): accessor(), load_glb(), main(), peak_summary(), quat_angle_deg(), rotation_stats(), vector_stats(), channel() (+2 more)

### Community 55 - "gaussian_diffusion.py"
Cohesion: 0.04
Nodes (18): _build_diffusion(), betas_for_alpha_bar(), get_named_beta_schedule(), LossType, ModelMeanType, ModelVarType, mean_flat(), sum_flat() (+10 more)

### Community 56 - "load_and_prep_asset"
Cohesion: 0.14
Nodes (9): clear_normal_maps(), clear_scene(), find_meshes(), fix_materials(), keep_armature_meshes(), keep_main_mesh_only(), load_and_prep_asset(), set_materials_opaque() (+1 more)

### Community 57 - "GraphAttnBias"
Cohesion: 0.09
Nodes (5): DiTBlock, FinalLayer, compute_graph_bias(), GraphAttnBias, UniMateGraphCrossAttn

### Community 59 - "Plotting Bin Helpers"
Cohesion: 0.16
Nodes (10): resolve_inputs(), ContactJoints, evaluate_clip(), find_ground_contact_joints(), load_cond_dicts(), main(), parse_args(), resolve_object_type() (+2 more)

### Community 60 - "os"
Cohesion: 0.15
Nodes (7): cond_from_rest(), preprocess_asset(), build_rest_animation(), build_topology_cond(), process_object(), process_tpose(), _save_tpose_vis()

### Community 61 - "Metadata I/O"
Cohesion: 0.17
Nodes (3): Logger, _CallerFileFormatter, zero_rank()

### Community 62 - "main"
Cohesion: 0.12
Nodes (9): _error_log_path(), _load_cached_result(), main(), _params_hash(), process_object_task(), _prune_object_clips(), resolve_category_groups(), build_stats() (+1 more)

### Community 64 - "blender_export.py"
Cohesion: 0.05
Nodes (33): _apply_root_rotation(), build_skeleton_arrays(), build_vertex_groups_sparse(), build_vgroup_to_bone_mapping(), children_from_parents(), choose_main_armature(), choose_main_mesh(), collapse_unused_root() (+25 more)

### Community 65 - "auto_label_unirig_quadruped_v2.original.py"
Cohesion: 0.18
Nodes (5): all_paths(), best_non_limb_path(), label_paw_branches(), lowest_path(), split_sides()

### Community 66 - "apply_skeleton_pooling"
Cohesion: 0.18
Nodes (5): apply_joint_removal(), apply_skeleton_pooling(), bone_length_weighted_sample(), build_children_map(), collapse_single_child_joint()

### Community 68 - "plot_dataset"
Cohesion: 0.12
Nodes (15): _apply_clip(), _joint_bins(), main(), parse_args(), plot_comparison(), plot_dataset(), print_table(), summarize() (+7 more)

### Community 69 - "Diffusion Loop Utilities"
Cohesion: 0.25
Nodes (5): compute_directions(), default_output_path(), load_motion_from_npz(), main(), render_skeleton_motion_directed()

### Community 71 - "argparse"
Cohesion: 0.08
Nodes (21): _action_bone_names(), _adopt_action(), animate_character_fbx(), parse_args(), parse_args(), parse_args(), parse_args(), animate_character() (+13 more)

### Community 72 - "cougar_nopost"
Cohesion: 0.20
Nodes (10): assets, cougar_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names (+2 more)

### Community 73 - "_build_spectral_encoder"
Cohesion: 0.13
Nodes (3): _build_spectral_encoder(), SignNetSpectralEncoder, WIRESpectralEncoder

### Community 74 - "Matplotlib Ticker Formatting"
Cohesion: 0.20
Nodes (3): handle_help(), print_usage(), _common.sh script

### Community 75 - "vis_tpose.py"
Cohesion: 0.19
Nodes (7): collect_keys_from_motions_dir(), default_single_output_path(), find_motion_npz(), load_tpose_from_npz(), main(), render_one(), save_skeleton_tpose_annotated()

### Community 79 - "metadata.py"
Cohesion: 0.19
Nodes (8): load_all_metadata(), load_category_groups(), load_clean_joint_names(), load_face_joint_names(), load_joint_names(), load_json(), load_motion_captions(), print_summary()

### Community 82 - "goat_nopost"
Cohesion: 0.22
Nodes (9): goat_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names, source (+1 more)

### Community 83 - "Metadata Lookup Helpers"
Cohesion: 0.29
Nodes (7): AgentOps, CONSEJO.md, HANDOFF_LATEST.md, MEMORIA.md, SKILL.md, STATUS.md, WORKFLOW.md

### Community 84 - "hippopotamus_nopost"
Cohesion: 0.22
Nodes (9): hippopotamus_nopost, canonical_glb, cond_key, cond_path, dataset, frame_digest, joint_names, source (+1 more)

### Community 85 - "render_mixamo.py"
Cohesion: 0.18
Nodes (6): main(), render_animated_file(), compose_frames_to_video(), enable_color_output(), render_action_multiview(), _reset_frames_dir()

### Community 86 - "render_tpose.py"
Cohesion: 0.22
Nodes (6): discover_assets(), main(), render_asset_tpose(), find_main_fbx(), sanitize_object_type(), init_render_engine()

### Community 88 - "Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets)"
Cohesion: 0.20
Nodes (9): 1. Criterio de Facing y Canonicalización, 2. Criterio de Texturas Embebidas, 3. Criterio de Ciclo Completo (2 Repeticiones), 4. Anclaje de Veredictos Visuales, Matriz de Trazabilidad Unificada — Lote quad10 (28 Assets), Resumen Ejecutivo de Trazabilidad, Rutas de Archivos Verificadas por Asset, Tabla de Trazabilidad de los 28 Assets (+1 more)

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
Cohesion: 0.12
Nodes (11): _anchor_for_dir(), _annotate_joints(), _box_aspect_from_bounds(), _edges_from_parents(), _fibonacci_sphere_dirs(), render_skeleton_spectral_grid(), render_skeleton_tpose_annotated(), _sample_bone_obstacles() (+3 more)

### Community 97 - "cougar_nopost-jump-rep_0-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_0-0.npy

### Community 113 - "cougar_nopost-jump-rep_1-0.npy"
Cohesion: 0.29
Nodes (7): asset, case_id, frame_digest, kind, prompt, run, cougar_nopost-jump-rep_1-0.npy

### Community 147 - "os"
Cohesion: 0.10
Nodes (12): _load(), main(), merge_summaries(), _save(), _scan_missing_frame_counts(), scan_clip_frames(), write_packed_images_to_dir(), _asset_marker_path() (+4 more)

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

### Community 164 - "save_skeleton_motion"
Cohesion: 0.21
Nodes (6): save_clip(), save_skeleton_motion(), save_skeleton_motion_ground(), save_skeleton_motion_spectral(), _write_video(), visualize_and_save_motions()

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

### Community 180 - "setup_lighting"
Cohesion: 0.33
Nodes (3): _create_light(), setup_lighting(), _setup_world_environment()

### Community 189 - "2026-11-02 21:55 +03:00 — dramatic catalogue wave started"
Cohesion: 0.10
Nodes (20): 2026-11-02 21:44 +03:00 — horse_nopost catalogue-verb feasibility test, 2026-11-02 21:47 +03:00 — dog canary plumbing failure caught pre-sampling, 2026-11-02 21:47 +03:00 — preflight passed; dog canary released, 2026-11-02 21:51 +03:00 — dog canary 1/2 QA complete, 2026-11-02 21:52 +03:00 — dog canary gate passed; remainder released, 2026-11-02 21:53 +03:00 — remainder input gate complete, 2026-11-02 21:55 +03:00 — dramatic catalogue wave started, 2026-11-02 22:04 +03:00 — remainder sampling progress (+12 more)

## Knowledge Gaps
- **25 isolated node(s):** `variants`, `graphify`, `FFmpeg`, `UniML3D Teaser Diagram`, `Stage 5: Mesh Animation` (+20 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1357 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **85 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseConditioner` connect `T5Conditioner` to `sample.py`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **What connects `variants`, `graphify`, `FFmpeg` to the rest of the system?**
  _25 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `preprocess_char.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0412280701754386 - nodes in this community are weakly interconnected._
- **Should `sys` be split into smaller, more focused modules?**
  _Cohesion score 0.08357685563997662 - nodes in this community are weakly interconnected._
- **Should `numpy` be split into smaller, more focused modules?**
  _Cohesion score 0.061367621274108705 - nodes in this community are weakly interconnected._
- **Should `dataset.py` be split into smaller, more focused modules?**
  _Cohesion score 0.059322033898305086 - nodes in this community are weakly interconnected._
- **Should `sample.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0782608695652174 - nodes in this community are weakly interconnected._