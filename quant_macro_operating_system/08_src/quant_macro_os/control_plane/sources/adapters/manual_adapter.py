class ManualAdapter:
    def fetch(self, config):
        return {
            "source_type": "manual",
            "records": config.get("records", []),
            "description": config.get("description", ""),
            "metadata": {},
        }
