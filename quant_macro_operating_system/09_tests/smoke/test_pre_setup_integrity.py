from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    "00_governance/adr_governance_policy.md",
    "00_governance/runtime_artifact_policy.md",
    "05_architecture/adr/ADR-0002-agent-architecture.md",
    "05_architecture/research_operating_flow.md",
    "06_research_engine/README.md",
    "08_src/quant_macro_os/control_plane/sources/source_templates.py",
    "08_src/quant_macro_os/control_plane/pipeline/pipeline_presets.py",
    "08_src/quant_macro_os/control_plane/services/system_state_service.py",
    "08_src/quant_macro_os/control_plane/ui/streamlit_app.py",
]
def test_required_files_exist():
    for rel in REQUIRED:
        assert (REPO_ROOT / rel).exists(), rel
def test_no_transient_artifacts():
    for path in REPO_ROOT.rglob("*"):
        rel = str(path.relative_to(REPO_ROOT))
        assert "__pycache__" not in rel
        assert ".pytest_cache" not in rel
        assert not rel.endswith(".pyc")
        assert not rel.endswith(".bak")
        assert not rel.endswith("system.log")
