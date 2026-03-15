from dataclasses import dataclass

@dataclass
class PerformanceSnapshot:
    performance_id: str
    portfolio_id: str
    timestamp: str
    realized_return: float
    realized_alpha: float
    transaction_cost: float
    edge_realization_score: float | None = None
