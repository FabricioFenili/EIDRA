from dataclasses import dataclass, field

@dataclass(slots=True)
class MetadataEnvelope:
    source_name: str
    source_instance: str
    data_family: str
    contract_name: str
    lineage: dict[str, str] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
