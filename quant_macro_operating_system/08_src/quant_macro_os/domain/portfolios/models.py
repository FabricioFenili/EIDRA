from dataclasses import dataclass, field

@dataclass
class Portfolio:
    portfolio_id: str
    timestamp: str
    weights: dict[str, float] = field(default_factory=dict)
    risk_profile: str = "standard"
