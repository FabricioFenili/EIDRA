from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(slots=True)
class PilotResearchPlan:
    source_name: str
    canonical_return_variable: str
    initial_features: list[str] = field(default_factory=list)
    initial_signal: str = "ptax_momentum_signal"
    initial_model: str = "ptax_momentum_baseline"

class ResearchBootstrapService:
    def build_ptax_plan(self) -> PilotResearchPlan:
        return PilotResearchPlan(
            source_name="petax_bacen_sgs",
            canonical_return_variable="usd_brl_log_return",
            initial_features=[
                "usd_brl_log_return",
                "usd_brl_volatility_20d",
                "usd_brl_momentum_20d",
                "usd_brl_momentum_60d",
                "usd_brl_momentum_120d",
                "usd_brl_drawdown",
            ],
        )

    def signal_band(self, percentile: float) -> str:
        if percentile < 20:
            return "very_weak"
        if percentile < 40:
            return "weak"
        if percentile < 60:
            return "neutral"
        if percentile < 80:
            return "strong"
        return "extreme"
