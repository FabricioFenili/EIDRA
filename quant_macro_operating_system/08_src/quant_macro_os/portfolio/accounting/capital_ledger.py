class CapitalLedger:
    def __init__(self):
        self._events = []

    def record_cashflow(self, event) -> None:
        self._events.append(event)

    def snapshot(self):
        return {"events": list(self._events)}
