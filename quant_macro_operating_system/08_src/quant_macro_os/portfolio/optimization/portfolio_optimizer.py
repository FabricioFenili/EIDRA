from __future__ import annotations

from typing import Dict

class PortfolioOptimizer:
    def optimize(self, expected_returns: Dict[str, float]) -> Dict[str, float]:
        total = sum(abs(v) for v in expected_returns.values()) or 1.0
        return {asset: value / total for asset, value in expected_returns.items()}
