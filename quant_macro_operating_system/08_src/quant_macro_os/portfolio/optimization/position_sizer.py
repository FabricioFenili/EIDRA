from __future__ import annotations

from typing import Dict

class PositionSizer:
    def size_positions(self, weights: Dict[str, float], capital: float) -> Dict[str, float]:
        return {asset: weight * capital for asset, weight in weights.items()}
