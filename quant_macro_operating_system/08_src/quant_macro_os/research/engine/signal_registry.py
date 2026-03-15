from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class SignalRecord:
    name: str
    description: str

class SignalRegistry:
    def register(self, signal_name: str, description: str) -> SignalRecord:
        return SignalRecord(name=signal_name, description=description)
