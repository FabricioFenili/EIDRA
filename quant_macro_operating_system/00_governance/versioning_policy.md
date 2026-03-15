# Versioning Policy

This project follows a strict institutional versioning rule.

## External Versioning

Version numbers are applied **only to distributed artifacts**, such as:

quant_macro_operating_system_vX.zip

Example:

quant_macro_operating_system_v7.zip
quant_macro_operating_system_v8.zip

## Internal Structure

The internal project root must **never contain version numbers**.

Correct:

quant_macro_operating_system/

Incorrect:

quant_macro_operating_system_v7/
quant_macro_operating_system_v8/

This guarantees:

- stable internal paths
- documentation consistency
- refactor safety
- reproducible builds

## Artifact Cleanliness

Before packaging:

- remove __pycache__
- remove *.pyc
- remove .pytest_cache

## Governance

This rule is mandatory for all future releases.