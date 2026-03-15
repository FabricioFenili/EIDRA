from dataclasses import dataclass

@dataclass
class Order:
    order_id: str
    portfolio_id: str
    asset_id: str
    side: str
    quantity: float
    order_type: str
    urgency: str
