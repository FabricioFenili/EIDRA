from __future__ import annotations

from typing import Dict

class ExposureManager:
    def enforce_limits(self, exposures: Dict[str, float], limit: float = 0.30) -> Dict[str, float]:
        return {asset: min(weight, limit) for asset, weight in exposures.items()}
