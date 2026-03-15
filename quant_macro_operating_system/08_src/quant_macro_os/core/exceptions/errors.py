class QMOSError(Exception):
    """Base project exception."""

class ConfigurationError(QMOSError):
    pass

class ContractViolationError(QMOSError):
    pass

class RoutingError(QMOSError):
    pass

class PublishError(QMOSError):
    pass
