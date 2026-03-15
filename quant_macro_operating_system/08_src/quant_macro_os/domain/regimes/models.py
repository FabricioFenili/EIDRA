from dataclasses import dataclass

@dataclass
class RegimeState:
    regime_id: str
    current_regime: str
    confidence: float
    transition_risk: float
