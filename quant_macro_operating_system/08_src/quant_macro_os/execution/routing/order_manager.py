from __future__ import annotations

from typing import Dict

class OrderManager:
    def create_orders(self, target_positions: Dict[str, float]) -> Dict[str, float]:
        return dict(target_positions)
