class RebalanceGovernor:
    def evaluate(self, portfolio_state):
        return {"status": "ok", "rebalance_required": False, "input": portfolio_state}
