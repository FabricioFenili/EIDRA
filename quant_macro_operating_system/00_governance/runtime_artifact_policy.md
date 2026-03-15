# Runtime Artifact Policy

Release artifacts must not contain runtime-generated files.

## Forbidden in release packages
- logs/system.log
- __pycache__
- .pytest_cache
- *.pyc
- *.bak

## Allowed
- empty runtime directories tracked only with `.gitkeep`

## Enforcement
Release candidates fail integrity validation if runtime residue is present.
