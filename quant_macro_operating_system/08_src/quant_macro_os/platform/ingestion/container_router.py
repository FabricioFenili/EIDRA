class ContainerRouter:
    def resolve_container(self, source_type: str) -> str:
        return source_type or "undefined"

    def route(self, source_record):
        return {"status": "ok", "container": self.resolve_container(source_record.get("source_type", "")), "source_record": source_record}
