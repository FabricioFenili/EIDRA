from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path

@dataclass(slots=True)
class RoleKnowledgeRoute:
    role_name: str
    canon_paths: list[str] = field(default_factory=list)
    repository_paths: list[str] = field(default_factory=list)

class RoleKnowledgeRoutingService:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root.resolve()
        self.routes = {
            "ceo_council": RoleKnowledgeRoute(
                "ceo_council",
                canon_paths=[
                    "12_docs/knowledge_pillars/executive_canon_ceo_council.md",
                    "12_docs/knowledge_pillars/knowledge_constitution.md",
                    "12_docs/knowledge_pillars/role_knowledge_routing_matrix.md",
                ],
                repository_paths=["00_governance", "01_constitutions", "12_docs"],
            ),
            "vp_quant_research": RoleKnowledgeRoute(
                "vp_quant_research",
                canon_paths=[
                    "12_docs/knowledge_pillars/vp_quant_research_canon.md",
                    "12_docs/research_doctrine/research_doctrine.md",
                    "12_docs/research_doctrine/factor_registry.md",
                ],
                repository_paths=["02_vps/01_quant_research", "08_src/quant_macro_os/research"],
            ),
            "vp_feature_engineering": RoleKnowledgeRoute(
                "vp_feature_engineering",
                canon_paths=[
                    "12_docs/knowledge_pillars/vp_feature_engineering_canon.md",
                    "12_docs/feature_governance/feature_drift_registry.md",
                ],
                repository_paths=["02_vps/02_feature_engineering", "08_src/quant_macro_os/features"],
            ),
            "vp_macro_intelligence": RoleKnowledgeRoute(
                "vp_macro_intelligence",
                canon_paths=[
                    "12_docs/knowledge_pillars/vp_macro_intelligence_canon.md",
                    "12_docs/macro_foundations/macro_causal_framework.md",
                ],
                repository_paths=["02_vps/03_macro_intelligence", "08_src/quant_macro_os/macro"],
            ),
            "vp_portfolio_construction": RoleKnowledgeRoute(
                "vp_portfolio_construction",
                canon_paths=[
                    "12_docs/knowledge_pillars/vp_portfolio_construction_canon.md",
                    "13_strategy/strategy_taxonomy.md",
                ],
                repository_paths=["02_vps/04_portfolio_construction", "08_src/quant_macro_os/portfolio"],
            ),
            "vp_risk_resilience": RoleKnowledgeRoute(
                "vp_risk_resilience",
                canon_paths=[
                    "12_docs/knowledge_pillars/vp_risk_resilience_canon.md",
                    "12_docs/risk_governance/alpha_decay_registry.md",
                    "12_docs/research_doctrine/model_retirement_policy.md",
                ],
                repository_paths=["02_vps/05_risk_resilience", "08_src/quant_macro_os/risk"],
            ),
        }

    def validate_route(self, role_name: str) -> dict:
        route = self.routes[role_name]
        missing = []
        for rel in route.canon_paths + route.repository_paths:
            if not (self.repo_root / rel).exists():
                missing.append(rel)
        return {"status": "ok" if not missing else "missing", "role_name": role_name, "missing": missing}

    def validate_all(self) -> list[dict]:
        return [self.validate_route(role) for role in sorted(self.routes)]
