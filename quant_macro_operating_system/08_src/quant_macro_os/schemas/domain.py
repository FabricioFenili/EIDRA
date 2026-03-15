from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

class AssetSchema(BaseModel):
    asset_id: str
    ticker: str
    asset_class: str
    currency: str
    country: str
    exchange: str
    sector: Optional[str] = None
    status: str = "active"

class FeatureSchema(BaseModel):
    feature_id: str
    feature_name: str
    feature_version: str
    entity_id: str
    timestamp: str
    value: float
    validation_status: bool = True

class SignalSchema(BaseModel):
    signal_id: str
    signal_name: str
    signal_score: float
    confidence: float = Field(ge=0.0, le=1.0)
    half_life: Optional[float] = None
    expected_return: Optional[float] = None

class RegimeStateSchema(BaseModel):
    regime_id: str
    current_regime: str
    confidence: float = Field(ge=0.0, le=1.0)
    transition_risk: float = Field(ge=0.0, le=1.0)

class ScenarioStateSchema(BaseModel):
    scenario_id: str
    scenario_name: str
    probability: float = Field(ge=0.0, le=1.0)

class PortfolioSchema(BaseModel):
    portfolio_id: str
    timestamp: str
    weights: dict[str, float]
    risk_profile: str

class OrderSchema(BaseModel):
    order_id: str
    portfolio_id: str
    asset_id: str
    side: str
    quantity: float
    order_type: str
    urgency: str

class TradeSchema(BaseModel):
    trade_id: str
    order_id: str
    executed_quantity: float
    executed_price: float
    venue: str
    execution_cost: float
    timestamp: str

class PerformanceSnapshotSchema(BaseModel):
    performance_id: str
    portfolio_id: str
    timestamp: str
    realized_return: float
    realized_alpha: float
    transaction_cost: float
    edge_realization_score: Optional[float] = None
