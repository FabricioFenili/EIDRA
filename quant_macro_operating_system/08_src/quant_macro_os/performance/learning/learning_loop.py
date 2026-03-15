class LearningLoop:
    def collect(self, decision_log):
        return {"status": "ok", "collected": decision_log}

    def prioritize(self):
        return {"status": "ok", "priorities": []}
