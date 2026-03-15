class FeatureBuilder:
    feature_family: str = "undefined"

    def build(self, dataset):
        return {"status": "ok", "feature_family": self.feature_family, "input": dataset}
