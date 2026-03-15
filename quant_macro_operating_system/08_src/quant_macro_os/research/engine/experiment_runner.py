from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

@dataclass(frozen=True)
class ExperimentResult:
    experiment: str
    status: str
    params: Dict[str, Any]

class ExperimentRunner:
    def run(self, experiment_name: str, params: Dict[str, Any]) -> ExperimentResult:
        return ExperimentResult(experiment=experiment_name, status="executed", params=params)
