from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class PipelineRecord:
    name: str
    owner: str
