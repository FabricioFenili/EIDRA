from dataclasses import dataclass

@dataclass(slots=True)
class FeatureDefinition:
    feature_name: str
    feature_family: str
    source_family: str
    contract_name: str

class FeatureDefinitionRegistry:
    def __init__(self):
        self._items: dict[str, FeatureDefinition] = {}

    def register(self, definition: FeatureDefinition) -> None:
        self._items[definition.feature_name] = definition

    def list_all(self):
        return list(self._items.values())
