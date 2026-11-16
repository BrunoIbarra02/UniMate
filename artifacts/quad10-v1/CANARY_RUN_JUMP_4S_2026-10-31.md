# Canary run+jump ~4 s — 2026-10-31

Estado: `human_review_required`. No implica aprobación técnica ni visual.

## Alcance y producción

- Especies/rigs congelados: `hippopotamus_nopost`, `goat_nopost`, `cougar_nopost`.
- Acciones: `run` (`An object runs in place.`) y `jump` (`An object jumps in place.`).
- Dos repeticiones por acción/especie: 12 clips.
- UniMate: `outputs/unimate_uniml3d_f60_v3/checkpoints/checkpoint_step_150000.pt`, CFG 3.0, seed 0.
- Expansión: 2 segmentos, overlap 10, `max_motion_length=60`, 110 frames latentes.
- Export real: 88 frames de animación GLB sobre timeline de 24 fps (~3.67 s).
- Preview final: 89 frames, 24 fps, 3.708333 s (`ffprobe`, idéntico en los 12 MP4).
- Canal S3: `s3://global-storage-491/unimate_pilots_20261018/{species}/animation_candidates/{action}_skintokens_quad10_cfg3_4s/rep_{0|1}.{glb|mp4}`.

Se verificaron los 24 objetos finales en S3. No se modificó `backend/app.py` ni se desplegó a ECS.

## QA automático quad10

Umbrales heredados: `edge_stretch_max <= 40`, `edge_stretch_p99_max <= 3.5`, `moving_leg_fraction >= 0.5`. Los 12 pasan esos tres gates; esto no sustituye revisión visual.

| Especie | Acción | Rep | Frames GLB | edge p99 | edge max | Patas móviles | seam RMS | Gate |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| cougar | jump | 0 | 88 | 2.0312 | 12.5984 | 10/16 | 0.0402 | pass |
| cougar | jump | 1 | 88 | 2.3187 | 10.9276 | 11/16 | 0.0592 | pass |
| cougar | run | 0 | 88 | 2.3923 | 8.6649 | 14/16 | 0.0537 | pass |
| cougar | run | 1 | 88 | 2.2700 | 15.4591 | 14/16 | 0.0823 | pass |
| goat | jump | 0 | 88 | 2.9327 | 12.2464 | 12/16 | 0.0501 | pass |
| goat | jump | 1 | 88 | 2.3206 | 27.5246 | 13/16 | 0.0570 | pass |
| goat | run | 0 | 88 | 2.4529 | 14.5170 | 13/16 | 0.1010 | pass |
| goat | run | 1 | 88 | 2.4587 | 28.7096 | 12/16 | 0.0605 | pass |
| hippopotamus | jump | 0 | 88 | 2.8588 | 19.0669 | 14/16 | 0.1072 | pass |
| hippopotamus | jump | 1 | 88 | 2.6276 | 27.0386 | 14/16 | 0.0711 | pass |
| hippopotamus | run | 0 | 88 | 2.6210 | 19.1558 | 14/16 | 0.0483 | pass |
| hippopotamus | run | 1 | 88 | 2.2994 | 16.5668 | 14/16 | 0.0556 | pass |

## Simetría

`validate_unimate_annotation.py --reviewed` dio cero issues en los tres rigs: hippopotamus 27 joints, goat 27, cougar 32. Este validador verifica pares/facing, conteos Left/Right y semántica del rig, no movimiento.

`compare_rig_quality.py` sí calcula simetría dinámica como `min(left,right)/max(left,right)` de la suma de rangos de rotación por miembro. El script conserva nombres históricos fijos; se ejecutó sin cambiar su algoritmo con el mapeo persistido `tiger→hippopotamus`, `deer→goat`, `horse→cougar`.

| Caso | Especie | Reposo front/hind | Movimiento front/hind |
|---|---|---|---|
| jump rep 0 | hippopotamus | 1.000 / 1.000 | 0.898 / 0.851 |
| jump rep 0 | goat | 1.000 / 0.998 | 0.905 / 0.994 |
| jump rep 0 | cougar | 0.999 / 1.000 | 0.953 / 0.927 |
| jump rep 1 | hippopotamus | 1.000 / 1.000 | 0.882 / 0.931 |
| jump rep 1 | goat | 1.000 / 0.998 | 0.642 / 0.883 |
| jump rep 1 | cougar | 0.999 / 1.000 | 0.768 / 0.902 |
| run rep 0 | hippopotamus | 1.000 / 1.000 | 0.617 / 0.771 |
| run rep 0 | goat | 1.000 / 0.998 | 0.933 / 0.735 |
| run rep 0 | cougar | 0.999 / 1.000 | 0.759 / 0.783 |
| run rep 1 | hippopotamus | 1.000 / 1.000 | 0.913 / 0.896 |
| run rep 1 | goat | 1.000 / 0.998 | 0.984 / 0.841 |
| run rep 1 | cougar | 0.999 / 1.000 | 0.950 / 0.942 |

La herramienta no define un umbral de aceptación para esos ratios. Se conservan como señal para revisión visual, especialmente `hippopotamus/run/rep_0` (front 0.617) y `goat/jump/rep_1` (front 0.642).

## Rutas de evidencia

- Remoto: `/home/ubuntu/skintokens_quad10_20261027/canary_run_jump_4s_20261031/`.
- Manifest y QA descargados: `tmp/quad10_canary_4s/results/`.
- Log operativo append-only: `C:\Users\htsy4\Desktop\AgentOps\unimate-animacion\debates\i-need-to-know-how-many-quadrupeds-we-have-and-if_1793458192\session_log_codex.md`.
- Contact sheets remotos: `.../canary_run_jump_4s_20261031/sheets/`.

`eval_foot_contact.py` no se usó como gate. El renderer histórico también forzaba 30 fps; se corrigió a 24 fps por defecto (override `QA_FPS`) y se rerenderizaron/reemplazaron los 12 MP4.
