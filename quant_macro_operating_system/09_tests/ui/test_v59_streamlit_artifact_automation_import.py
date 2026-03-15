from quant_macro_os.control_plane.ui.streamlit_app import build_app

def test_v59_streamlit_app_importable():
    assert callable(build_app)
