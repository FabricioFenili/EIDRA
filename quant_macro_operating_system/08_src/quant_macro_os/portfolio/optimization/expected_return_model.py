from __future__ import annotations

from typing import Dict

class ExpectedReturnModel:
    def estimate(self, signals: Dict[str, float]) -> Dict[str, float]:
        return dict(signals)
