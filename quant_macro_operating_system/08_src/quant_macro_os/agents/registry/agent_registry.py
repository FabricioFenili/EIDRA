from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional

AGENT_LEVELS = ["vp", "director", "superintendent", "manager", "coordinator", "specialist"]


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    level: str
    domain: str
    scope: List[str] = field(default_factory=list)
    reports_to: Optional[str] = None


class AgentRegistry:
    def __init__(self) -> None:
        self._agents: Dict[str, AgentDefinition] = {}

    def register(self, agent: AgentDefinition) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> AgentDefinition:
        return self._agents[name]

    def exists(self, name: str) -> bool:
        return name in self._agents

    def by_domain(self, domain: str, *, level: Optional[str] = None) -> List[AgentDefinition]:
        agents = [a for a in self._agents.values() if a.domain == domain]
        if level is not None:
            agents = [a for a in agents if a.level == level]
        return sorted(agents, key=lambda a: (a.level, a.name))

    def by_level(self, level: str) -> List[AgentDefinition]:
        return sorted([a for a in self._agents.values() if a.level == level], key=lambda a: a.name)

    def search_scope(self, text: str, *, domain: Optional[str] = None) -> List[AgentDefinition]:
        low = text.lower()
        matches: List[AgentDefinition] = []
        for agent in self._agents.values():
            if domain is not None and agent.domain != domain:
                continue
            haystack = " ".join(agent.scope).lower()
            if any(token in haystack for token in low.split()):
                matches.append(agent)
        return sorted(matches, key=lambda a: (a.level, a.name))

    def all(self) -> Iterable[AgentDefinition]:
        return self._agents.values()


def build_default_registry() -> AgentRegistry:
    registry = AgentRegistry()

    defaults = [
        AgentDefinition("vp_quant_research", "vp", "research", ["alpha", "signal", "backtest"]),
        AgentDefinition("vp_feature_engineering", "vp", "features", ["dataset", "feature", "leakage", "drift"]),
        AgentDefinition("vp_macro_intelligence", "vp", "macro", ["regime", "inflation", "growth", "liquidity"]),
        AgentDefinition("vp_portfolio_construction", "vp", "portfolio", ["allocation", "kelly", "optimization", "weights"]),
        AgentDefinition("vp_risk_resilience", "vp", "risk", ["drawdown", "stress", "tail", "ruin"]),
        AgentDefinition("vp_execution_microstructure", "vp", "execution", ["slippage", "routing", "impact", "microstructure"]),
        AgentDefinition("vp_performance_learning", "vp", "performance", ["attribution", "postmortem", "learning"]),
        AgentDefinition("director_signal_discovery", "director", "research", ["signal discovery", "hypothesis generation"], "vp_quant_research"),
        AgentDefinition("director_econometric_validation", "director", "research", ["econometric validation", "time series", "cross-sectional"], "vp_quant_research"),
        AgentDefinition("director_feature_construction", "director", "features", ["feature construction", "rolling features", "macro derived"], "vp_feature_engineering"),
        AgentDefinition("director_growth_inflation", "director", "macro", ["growth", "inflation", "nowcasting", "regime"], "vp_macro_intelligence"),
        AgentDefinition("director_optimization_sizing", "director", "portfolio", ["optimization", "kelly sizing", "rebalancing"], "vp_portfolio_construction"),
        AgentDefinition("director_tail_ruin_risk", "director", "risk", ["tail risk", "ruin probability", "drawdown"], "vp_risk_resilience"),
        AgentDefinition("director_execution_algorithms", "director", "execution", ["twap", "vwap", "scheduling"], "vp_execution_microstructure"),
        AgentDefinition("director_performance_attribution", "director", "performance", ["alpha beta factor attribution", "decision quality"], "vp_performance_learning"),
        AgentDefinition("specialist_signal_screening", "specialist", "research", ["signal screening", "triage", "factors"], "director_signal_discovery"),
        AgentDefinition("specialist_econometric_diagnostics", "specialist", "research", ["arima", "diagnostics", "stationarity", "validation"], "director_econometric_validation"),
        AgentDefinition("specialist_feature_leakage_control", "specialist", "features", ["leakage", "temporal integrity", "lineage"], "director_feature_construction"),
        AgentDefinition("specialist_regime_classifier", "specialist", "macro", ["inflation regime", "growth regime", "liquidity"], "director_growth_inflation"),
        AgentDefinition("specialist_kelly_optimizer", "specialist", "portfolio", ["kelly", "optimization", "allocation"], "director_optimization_sizing"),
        AgentDefinition("specialist_tail_risk_model", "specialist", "risk", ["tail risk", "stress testing", "ruin"], "director_tail_ruin_risk"),
        AgentDefinition("specialist_execution_cost_model", "specialist", "execution", ["slippage", "impact", "transaction cost"], "director_execution_algorithms"),
        AgentDefinition("specialist_postmortem_analyst", "specialist", "performance", ["attribution", "postmortem", "thesis quality"], "director_performance_attribution"),
    ]
    for agent in defaults:
        registry.register(agent)
    return registry


DEFAULT_REGISTRY = build_default_registry()
AGENT_REGISTRY = {a.name: {"level": a.level, "domain": a.domain} for a in DEFAULT_REGISTRY.all()}
SKILL_MATRIX = {a.name: {"domain": a.domain, "scope": a.scope} for a in DEFAULT_REGISTRY.all() if a.level == "specialist"}
