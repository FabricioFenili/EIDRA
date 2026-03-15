from dataclasses import dataclass

@dataclass(slots=True)
class LayerContract:
    layer_name: str
    expected_grain: str
    contract_name: str
    description: str
