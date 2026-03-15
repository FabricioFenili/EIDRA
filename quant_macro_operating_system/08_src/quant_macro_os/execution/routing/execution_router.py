from __future__ import annotations

from typing import Dict

class ExecutionRouter:
    def route(self, orders: Dict[str, float], venue: str = "PRIMARY") -> Dict[str, Dict[str, float | str]]:
        return {asset: {"quantity": qty, "venue": venue} for asset, qty in orders.items()}
