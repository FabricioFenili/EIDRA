class RunMonitor:
    def __init__(self):
        self._runs = {}

    def open_run(self, run_name: str) -> str:
        run_id = f"run::{run_name}"
        self._runs[run_id] = "open"
        return run_id

    def close_run(self, run_id: str, status: str) -> None:
        self._runs[run_id] = status
