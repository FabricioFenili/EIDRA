from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_v57_brand_integration_present():
    assert (REPO_ROOT / "14_marketing_strategy" / "v57_brand_integration_manifest.md").exists()
    assert (REPO_ROOT / "14_marketing_strategy" / "v57_brand_governance_binding.md").exists()
    assert (REPO_ROOT / "14_marketing_strategy" / "brand_system_v56_integrated").exists()
