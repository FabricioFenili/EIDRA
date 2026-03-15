from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

@dataclass
class MetadataRegistry:
    datasets: Dict[str, str] = field(default_factory=dict)
    features: Dict[str, str] = field(default_factory=dict)
    pipelines: Dict[str, str] = field(default_factory=dict)
    experiments: Dict[str, str] = field(default_factory=dict)

    def register_dataset(self, name: str, source: str) -> None:
        self.datasets[name] = source

    def register_feature(self, name: str, description: str) -> None:
        self.features[name] = description

    def register_pipeline(self, name: str, owner: str) -> None:
        self.pipelines[name] = owner

    def register_experiment(self, name: str, summary: str) -> None:
        self.experiments[name] = summary
