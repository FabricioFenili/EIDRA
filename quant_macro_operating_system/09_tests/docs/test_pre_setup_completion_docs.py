from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def test_completion_docs_exist():
    required = [
        "12_docs/knowledge_pillars/knowledge_constitution.md",
        "12_docs/knowledge_pillars/role_knowledge_routing_matrix.md",
        "12_docs/knowledge_pillars/directorate_knowledge_matrix.md",
        "12_docs/knowledge_pillars/superintendency_knowledge_matrix.md",
        "12_docs/research_doctrine/research_doctrine.md",
        "12_docs/research_doctrine/factor_registry.md",
        "12_docs/research_doctrine/model_retirement_policy.md",
        "12_docs/feature_governance/feature_drift_registry.md",
        "12_docs/macro_foundations/macro_causal_framework.md",
        "12_docs/risk_governance/alpha_decay_registry.md",
        "13_strategy/strategy_taxonomy.md",
        "00_governance/decision_intelligence/decision_ledger.md",
        "00_governance/decision_intelligence/research_capital_allocation.md",
        "12_docs/pre_setup_completion_standard.md",
    ]
    for rel in required:
        assert (REPO_ROOT / rel).exists(), rel
