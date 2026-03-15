class ExecutionGovernor:
    def authorize(self, order_plan):
        return {"status": "ok", "authorized": True, "order_plan": order_plan}
