# Repository Standards

This document defines structural standards for the repository.

## Root Structure

quant_macro_operating_system/

00_governance
01_constitutions
02_vps
03_interfaces
04_ledgers_and_registries
05_architecture
06_operating_models
07_data_platform
08_src
09_tests
10_notebooks
11_runs
12_docs
99_archive

## Naming Rules

- lowercase
- underscores instead of spaces
- no version numbers in internal folders

## Documentation

All architecture and governance rules must be stored under:

00_governance
05_architecture
12_docs

## Clean Repository

Repository must not include:

- __pycache__
- compiled python files
- temporary experiment outputs