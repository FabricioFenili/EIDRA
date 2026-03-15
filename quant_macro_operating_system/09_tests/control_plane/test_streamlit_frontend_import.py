from quant_macro_os.control_plane.ui.streamlit_app import build_app

def test_streamlit_build_app_symbol_exists():
    assert callable(build_app)
