# Control Plane Security Boundaries

Allowed:
- parameter management
- pipeline triggering
- diff preview
- syntax validation
- staged patch apply
- rollback
- audit persistence

Forbidden:
- destructive shell commands
- blind overwrite without preview
- patch apply without validation
