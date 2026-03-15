from dataclasses import dataclass

@dataclass
class Signal:
    signal_id: str
    signal_name: str
    signal_score: float
    confidence: float
    half_life: float | None = None
    expected_return: float | None = None
