# Control Plane Runbook

## Start
`streamlit run 08_src/quant_macro_os/control_plane/ui/streamlit_app.py`

## Environment Variables
- `QMOS_REPO_ROOT`
- `QMOS_CONTROL_PLANE_DB`
- `QMOS_CONTROL_PLANE_WORKDIR`
- `QMOS_LOG_DIR`

## Flow
Browse file -> preview diff -> validate -> run tests -> apply -> rollback if needed.
