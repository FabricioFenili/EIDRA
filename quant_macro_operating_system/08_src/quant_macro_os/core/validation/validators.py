class BaseValidator:
    def validate(self, payload) -> None:
        return None

class ContractValidator(BaseValidator):
    pass

class FreshnessValidator(BaseValidator):
    pass

class JoinKeyValidator(BaseValidator):
    pass
