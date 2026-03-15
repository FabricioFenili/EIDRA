class FeatureStore:
    def __init__(self):
        self._items = {}

    def publish(self, feature_frame, version: str) -> None:
        self._items[version] = feature_frame

    def load(self, feature_family: str, version: str):
        return self._items.get(version, {"feature_family": feature_family, "version": version, "status": "missing"})
