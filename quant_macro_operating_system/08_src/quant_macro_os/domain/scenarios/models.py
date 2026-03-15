from dataclasses import dataclass

@dataclass
class ScenarioState:
    scenario_id: str
    scenario_name: str
    probability: float
