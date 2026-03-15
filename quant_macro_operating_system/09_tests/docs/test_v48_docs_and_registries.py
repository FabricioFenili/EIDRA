from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_v48_docs_and_registries_exist():
    required = [
        "12_docs/quant_research_foundations.md",
        "12_docs/signal_calibration_framework.md",
        "12_docs/first_pilot_source_ptax_usdbrl.md",
        "06_operating_models/feature_factory_operating_model.md",
        "06_operating_models/research_factory_operating_model.md",
        "06_operating_models/model_factory_operating_model.md",
        "07_data_platform/feature_registry.yaml",
        "07_data_platform/signal_registry.yaml",
        "07_data_platform/model_registry.yaml",
        "07_data_platform/contracts/datasets/data_source_contract.yaml",
        "10_notebooks/research/research_notebook_template.ipynb",
    ]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), rel
