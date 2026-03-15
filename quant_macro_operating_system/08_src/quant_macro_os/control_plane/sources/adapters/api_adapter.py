class APIAdapter:
    def fetch(self, config):
        return {
            "source_type": "api",
            "endpoint": config.get("endpoint", ""),
            "params": config.get("params", {}),
            "payload": config.get("mock_payload", []),
            "metadata": {"provider": config.get("provider", "")},
        }
