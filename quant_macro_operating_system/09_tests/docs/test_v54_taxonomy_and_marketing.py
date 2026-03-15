from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_v54_marketing_and_sequential_taxonomy_present():
    required_dirs = [
        "00_governance",
        "01_constitutions",
        "02_vps",
        "03_interfaces",
        "04_ledgers_and_registries",
        "05_architecture",
        "06_operating_models",
        "06_research_engine",
        "07_data_platform",
        "08_src",
        "09_tests",
        "10_notebooks",
        "11_runs",
        "12_docs",
        "13_strategy",
        "14_marketing_strategy",
        "99_archive",
    ]
    for rel in required_dirs:
        assert (REPO_ROOT / rel).exists(), rel

    required_files = [
        "14_marketing_strategy/README.md",
        "14_marketing_strategy/brand_architecture_governance.md",
        "14_marketing_strategy/marketing_operating_model.md",
        "14_marketing_strategy/scientific_communication_protocol.md",
        "14_marketing_strategy/product_positioning_framework.md",
        "14_marketing_strategy/distribution_strategy.md",
        "14_marketing_strategy/revenue_model_architecture.md",
        "14_marketing_strategy/commercialization_hierarchy.md",
        "12_docs/v54_taxonomy_integrity_note.md",
    ]
    for rel in required_files:
        assert (REPO_ROOT / rel).exists(), rel
