class StepExecutor:
    SUPPORTED_STEPS = {"source", "ingest", "normalize", "validate", "curate", "feature", "publish"}

    def execute(self, source_payload, steps, runtime_params):
        state = {
            "source_payload": source_payload,
            "runtime_params": runtime_params,
            "steps_executed": [],
            "unsupported_steps": [],
            "published": False,
        }
        for step in steps:
            if step not in self.SUPPORTED_STEPS:
                state["unsupported_steps"].append(step)
                continue
            state["steps_executed"].append(step)
            if step == "publish":
                state["published"] = True
        state["status"] = "ok" if not state["unsupported_steps"] else "partial"
        return state
