from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class BacktestResult:
    signal: str
    observations: int
    status: str

class BacktestEngine:
    def run_backtest(self, signal_name: str, dataset: Sequence[float]) -> BacktestResult:
        return BacktestResult(signal=signal_name, observations=len(dataset), status="completed")
