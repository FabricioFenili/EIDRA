from dataclasses import dataclass

@dataclass
class Asset:
    asset_id: str
    ticker: str
    asset_class: str
    currency: str
    country: str
    exchange: str
    sector: str | None = None
    status: str = "active"
