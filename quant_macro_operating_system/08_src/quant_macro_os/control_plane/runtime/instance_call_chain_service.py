from dataclasses import dataclass, field

@dataclass(slots=True)
class InstanceCall:
    instance_name: str
    service_name: str
    contract_name: str
    depends_on: list[str] = field(default_factory=list)

class InstanceCallChainService:
    def build_chain(self, instance_name: str) -> list[InstanceCall]:
        return [
            InstanceCall(instance_name, "runtime_scheduler", "schedule_policy_v1", []),
            InstanceCall(instance_name, "pipeline_controller", "pipeline_runtime_v1", ["runtime_scheduler"]),
            InstanceCall(instance_name, "platinum_service", "platinum_domain_model_v1", ["pipeline_controller"]),
        ]

    def validate_chain(self, instance_name: str) -> None:
        chain = self.build_chain(instance_name)
        if not chain:
            raise ValueError("empty_instance_chain")
