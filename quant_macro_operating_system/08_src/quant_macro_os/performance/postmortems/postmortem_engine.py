class PostmortemEngine:
    def analyze(self, failed_decision):
        return {"status": "ok", "analysis": {}, "input": failed_decision}
