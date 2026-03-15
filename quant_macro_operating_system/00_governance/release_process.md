# Release Process

This document defines the institutional release process for the Quant Macro Operating System.

## Steps for a New Release

1. Ensure repository passes tests
2. Clean transient artifacts:
   - __pycache__
   - *.pyc
   - .pytest_cache
3. Validate documentation integrity
4. Generate artifact using versioned filename

Example:

quant_macro_operating_system_vX.zip

5. Generate repository tree snapshot:

quant_macro_operating_system_vX_tree.txt

6. Store artifacts in release archive.

## Governance

All releases must follow the versioning_policy.md.