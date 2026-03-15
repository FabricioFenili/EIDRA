class ExecutionAlgorithm:
    algorithm_name: str = "undefined"

    def schedule(self, order):
        return {"status": "ok", "algorithm_name": self.algorithm_name, "order": order}
