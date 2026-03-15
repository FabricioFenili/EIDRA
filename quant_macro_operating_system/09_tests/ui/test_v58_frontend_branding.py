from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_v58_frontend_brand_assets_and_theme_present():
    required = [
        "14_marketing_strategy/brand_system_v57_integrated/eidra_logo_primary_v56.png",
        "14_marketing_strategy/brand_system_v57_integrated/eidra_monogram_v56.png",
        "14_marketing_strategy/brand_system_v57_integrated/eidra_favicon_64_v56.png",
        "14_marketing_strategy/brand_theme_tokens.json",
        "14_marketing_strategy/v58_frontend_brand_binding.md",
        "08_src/quant_macro_os/control_plane/ui/streamlit_app.py",
    ]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), rel

def test_v58_streamlit_app_references_brand_assets():
    app = (REPO_ROOT / "08_src/quant_macro_os/control_plane/ui/streamlit_app.py").read_text(encoding="utf-8")
    assert "_resolve_brand_asset" in app
    assert "_apply_brand_theme" in app
    assert "_render_brand" in app
    assert "eidra_logo_primary_v56.png" in app
    assert "eidra_monogram_v56.png" in app
    assert "eidra_favicon_64_v56.png" in app
