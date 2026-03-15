class PlatinumService:
    def __init__(self):
        self._models = {}

    def materialize_domain_model(self, model_name: str, payload) -> None:
        self._models[model_name] = payload

    def load_domain_model(self, model_name: str):
        return self._models.get(model_name, {"status": "missing", "model_name": model_name})
