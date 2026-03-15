import importlib.util
from pathlib import Path

def test_v60_streamlit_ui_bootstraps_package_path():
    path = Path(__file__).resolve().parents[2] / "08_src/quant_macro_os/control_plane/ui/streamlit_app.py"
    spec = importlib.util.spec_from_file_location("v60_streamlit_app", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, "build_app")
