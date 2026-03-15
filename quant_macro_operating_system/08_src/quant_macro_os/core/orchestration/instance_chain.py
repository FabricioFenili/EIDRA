from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class ChainStep:
    step_name: str
    service_name: str
    input_contract: str
    output_contract: str

@dataclass(slots=True)
class InstanceChainPlan:
    chain_name: str
    instance_name: str
    steps: list[ChainStep] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

class InstanceChainExecutor:
    def plan(self, instance_name: str) -> InstanceChainPlan:
        return InstanceChainPlan(
            chain_name=f"{instance_name}_default_chain",
            instance_name=instance_name,
            steps=[
                ChainStep("source", "source_executor", "raw_source_v1", "ingested_source_v1"),
                ChainStep("publish", "platinum_service", "platinum_candidate_v1", "platinum_domain_model_v1"),
            ],
            metadata={"mode": "noop"},
        )

    def execute(self, plan: InstanceChainPlan) -> dict[str, Any]:
        return {
            "status": "ok",
            "chain_name": plan.chain_name,
            "instance_name": plan.instance_name,
            "steps": [step.step_name for step in plan.steps],
            "mode": "noop",
        }
