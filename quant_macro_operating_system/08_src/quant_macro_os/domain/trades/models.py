from dataclasses import dataclass

@dataclass
class Trade:
    trade_id: str
    order_id: str
    executed_quantity: float
    executed_price: float
    venue: str
    execution_cost: float
    timestamp: str
