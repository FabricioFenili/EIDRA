class PlanningService:
    def build_execution_blueprint(self, instance_name: str):
        return {"status": "ok", "instance_name": instance_name, "blueprint": []}
