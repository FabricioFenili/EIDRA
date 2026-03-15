class SourceOnboardingService:
    def __init__(self):
        self.containers = set()
        self.families = set()

    def register_container(self, container_name: str) -> None:
        self.containers.add(container_name)

    def register_source_family(self, family_name: str) -> None:
        self.families.add(family_name)
