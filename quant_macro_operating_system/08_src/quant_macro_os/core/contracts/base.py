from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class ContractEnvelope:
    contract_name: str
    schema_version: str
    payload: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.contract_name:
            raise ValueError("contract_name_required")
        if not self.schema_version:
            raise ValueError("schema_version_required")
