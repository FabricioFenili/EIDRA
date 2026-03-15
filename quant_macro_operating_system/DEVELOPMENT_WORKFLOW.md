# DEVELOPMENT WORKFLOW

## Purpose

This document defines the mandatory engineering workflow for evolving the system without losing traceability, stability, or architectural coherence.

`BOOTSTRAP.md` explains **how to start the system**.

This document explains **how to change the system**.

## Branch strategy

- `main` — stable baseline
- `develop` — integration branch
- `feature/<name>` — new work
- `fix/<name>` — bug fix
- `docs/<name>` — documentation updates

## Standard flow

1. Pull the latest changes
2. Create a branch from `develop`
3. Implement the change
4. Run formatting, lint, and tests
5. Commit with the approved convention
6. Push the branch
7. Open a PR into `develop`
8. Merge only when checks pass

## Branch creation

```bash
git checkout develop
git pull
git checkout -b feature/<short-name>
```

## Commit convention

Use clear structured commits:

- `feat:` new capability
- `fix:` bug correction
- `refactor:` internal improvement without behavioral change
- `docs:` documentation only
- `test:` tests added or updated
- `build:` packaging or dependency changes
- `chore:` non-functional maintenance

Examples:

```bash
git commit -m "feat: add pipeline execution registry schema"
git commit -m "docs: add data platform operating rules"
```

## Pull request rules

Before opening a PR:

- run `make format`
- run `make lint`
- run `make test`
- confirm the change follows architecture and contracts
- update docs if behavior changes
- update or add tests if logic changes
- register major architecture decisions in ADRs when needed

## Definition of done

A change is complete only when:

- code works
- tests pass
- docs are updated when required
- contracts remain consistent
- no sensitive local state is committed
- architectural consequences are documented when the change is structural

## PyCharm discipline

PyCharm should be configured to:

- use `.venv/bin/python`
- run pytest
- respect project formatting settings
- avoid committing `.idea/`

## Versioning

Use semantic-style tags when the project matures:

- `v0.1.0`
- `v0.2.0`
- `v1.0.0`

## What must not happen

- direct pushes to `main`
- ambiguous commits like `fix2`, `update`, `final_now`
- architecture changes without documented rationale
- committing local data lake, SQLite, DuckDB, or artifacts

## Architecture governance trigger

Create or update an ADR when a change affects:

- data architecture
- repository structure
- control plane design
- feature registry logic
- experiment governance
- orchestration model

## Minimum cycle

```text
pull
branch
code
format
lint
test
commit
push
PR
```

## Goal

The purpose of this workflow is to make the repository a governed software factory, not just a folder of files.
