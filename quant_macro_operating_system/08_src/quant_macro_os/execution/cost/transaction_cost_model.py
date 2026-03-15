from __future__ import annotations

from typing import Dict

class TransactionCostModel:
    def estimate(self, orders: Dict[str, float], basis_points: float = 5.0) -> Dict[str, float]:
        return {asset: abs(qty) * (basis_points / 10_000.0) for asset, qty in orders.items()}
