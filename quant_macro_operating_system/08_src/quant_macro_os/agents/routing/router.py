from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Sequence, Tuple

from quant_macro_os.agents.contracts.models import TaskEnvelope

DOMAIN_KEYWORDS: Dict[str, Sequence[str]] = {
    "research": ["signal", "alpha", "backtest", "econometric", "factor", "fator", "research", "pesquisa"],
    "features": ["feature", "dataset", "dados", "leakage", "drift", "schema", "pipeline"],
    "macro": ["regime", "scenario", "cenário", "inflation", "inflação", "growth", "crescimento", "liquidity", "liquidez", "policy", "macro"],
    "portfolio": ["allocation", "alocação", "weights", "pesos", "optimization", "otimização", "kelly", "rebalancing", "portfólio", "portfolio"],
    "risk": ["drawdown", "ruin", "stress", "tail risk", "risco", "liquidity risk", "volatility", "survival"],
    "execution": ["order", "ordem", "slippage", "impact", "routing", "microstructure", "execution", "execução"],
    "performance": ["attribution", "performance", "postmortem", "post-mortem", "learning", "aprendizado", "decision quality"],
}

VP_BY_DOMAIN = {
    "research": "vp_quant_research",
    "features": "vp_feature_engineering",
    "macro": "vp_macro_intelligence",
    "portfolio": "vp_portfolio_construction",
    "risk": "vp_risk_resilience",
    "execution": "vp_execution_microstructure",
    "performance": "vp_performance_learning",
}


class AgentRouter:
    def __init__(self, domain_keywords: Dict[str, Sequence[str]] | None = None) -> None:
        self.domain_keywords = dict(domain_keywords or DOMAIN_KEYWORDS)

    def _score(self, request: str) -> List[Tuple[str, int]]:
        low = request.lower()
        scores: Dict[str, int] = defaultdict(int)
        for domain, keywords in self.domain_keywords.items():
            for keyword in keywords:
                if keyword in low:
                    scores[domain] += 1
        if not scores:
            return [("research", 0)]
        ordered = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        return ordered

    def route(self, task_id: str, request: str) -> TaskEnvelope:
        scores = self._score(request)
        primary_domain = scores[0][0]
        supporting_domains = [domain for domain, score in scores[1:] if score > 0][:3]
        acceptance = [
            "deliver evidence-based synthesis",
            "respect agent delegation chain",
            "record institutional timestamps",
        ]
        return TaskEnvelope(
            task_id=task_id,
            originating_user_request=request,
            routed_vp=VP_BY_DOMAIN[primary_domain],
            supporting_vps=[VP_BY_DOMAIN[d] for d in supporting_domains],
            priority="high" if len(supporting_domains) >= 2 else "normal",
            acceptance_criteria=acceptance,
            metadata={"primary_domain": primary_domain, "routing_mode": "keyword_consensus"},
        )


def route_to_vp(task_id: str, request: str) -> TaskEnvelope:
    return AgentRouter().route(task_id, request)
