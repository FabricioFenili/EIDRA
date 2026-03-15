from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class FeatureRecord:
    name: str
    description: str
