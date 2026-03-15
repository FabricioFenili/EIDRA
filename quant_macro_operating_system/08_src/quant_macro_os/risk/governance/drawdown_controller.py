from __future__ import annotations

from typing import Sequence

class DrawdownController:
    def check_drawdown(self, equity_curve: Sequence[float], limit: float = 0.20) -> Dict[str, float | bool]:
        if not equity_curve:
            return {"max_drawdown": 0.0, "limit_breached": False}
        peak = equity_curve[0]
        max_drawdown = 0.0
        for value in equity_curve:
            peak = max(peak, value)
            drawdown = (peak - value) / peak if peak else 0.0
            max_drawdown = max(max_drawdown, drawdown)
        return {"max_drawdown": max_drawdown, "limit_breached": max_drawdown > limit}
