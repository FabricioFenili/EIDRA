from dataclasses import dataclass, field

@dataclass(slots=True)
class ServiceNode:
    node_name: str
    service_type: str
    dependencies: list[str] = field(default_factory=list)

class ServiceGraph:
    def __init__(self):
        self._nodes: dict[str, ServiceNode] = {}

    def register(self, node: ServiceNode) -> None:
        self._nodes[node.node_name] = node

    def topological_order(self) -> list[str]:
        return list(self._nodes.keys())
