class ChainOfInstancesWorkflow:
    def build(self, root_instance: str):
        return {"status": "ok", "root_instance": root_instance, "chain": []}

    def dispatch(self, root_instance: str):
        return {"status": "ok", "root_instance": root_instance, "dispatched": True}
