from __future__ import annotations

from typing import Dict

class RiskModel:
    def evaluate(self, positions: Dict[str, float]) -> Dict[str, object]:
        total = sum(abs(v) for v in positions.values()) or 1.0
        exposures = {asset: value / total for asset, value in positions.items()}
        return {"total_exposure": total, "normalized_exposures": exposures}
