from dataclasses import dataclass

@dataclass
class Feature:
    feature_id: str
    feature_name: str
    feature_version: str
    entity_id: str
    timestamp: str
    value: float
    validation_status: bool = True
