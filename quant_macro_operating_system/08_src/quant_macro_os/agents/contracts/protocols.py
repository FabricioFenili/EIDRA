from dataclasses import dataclass

@dataclass(slots=True)
class AgentCall:
    caller: str
    callee: str
    topic: str
    payload_contract: str

class AgentProtocol:
    def handoff(self, call: AgentCall):
        return {"status": "ok", "call": call}
