from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class ExperimentRecord:
    name: str
    summary: str
