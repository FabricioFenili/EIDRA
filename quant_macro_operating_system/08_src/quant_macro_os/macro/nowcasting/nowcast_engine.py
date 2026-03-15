class NowcastEngine:
    def fit(self, dataset) -> None:
        self._fitted = True

    def predict(self, horizon: str):
        return {"status": "ok", "horizon": horizon, "mode": "noop"}
