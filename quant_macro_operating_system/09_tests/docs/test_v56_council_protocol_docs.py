from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_v56_council_protocol_documents_exist():
    required = [
        "00_governance/council_response_protocol_v56.md",
        "00_governance/council_invocation_standard_v56.md",
        "00_governance/founder_authority_precedence_v56.md",
    ]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), rel
