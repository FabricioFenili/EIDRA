# V60 Bootstrap and Runtime

V60 hardens the first-run experience.

## Startup
Preferred command from project root:
`python run_control_plane.py`

This launcher configures:
- PYTHONNOUSERSITE=1
- QMOS_REPO_ROOT
- QMOS_CONTROL_PLANE_DB
- QMOS_CONTROL_PLANE_WORKDIR
- sys.path for quant_macro_os

## Streamlit robustness
The UI now bootstraps `08_src` into sys.path automatically.

## Logging robustness
System logger falls back across writable directories instead of failing on a single unwritable path.

## Governance UX
The control plane now supports:
- save project
- delete project
- save source
- delete source
- canonical governance registration
- runtime registration
- artifact generation
