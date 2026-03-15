class SchemaRegistry:
    def __init__(self):
        self._schemas = {}

    def register(self, schema_name: str, schema_version: str, definition: dict) -> None:
        self._schemas[(schema_name, schema_version)] = definition

    def resolve(self, schema_name: str, schema_version: str) -> dict:
        return self._schemas.get((schema_name, schema_version), {})
