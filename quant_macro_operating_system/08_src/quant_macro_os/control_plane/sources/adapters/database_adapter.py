class DatabaseAdapter:
    def fetch(self, config):
        return {
            "source_type": "database",
            "connection_string": config.get("connection_string", ""),
            "query": config.get("query", ""),
            "rows": config.get("mock_rows", []),
            "metadata": {},
        }
