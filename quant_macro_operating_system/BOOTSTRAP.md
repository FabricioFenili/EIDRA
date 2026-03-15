# BOOTSTRAP

## Purpose

This document defines the official initialization procedure for a new local machine after cloning the repository.

It is the mandatory operating procedure for getting the project running in a reproducible way.

## Assumptions

- Linux Mint or equivalent Linux environment
- Python 3.9 available
- Git installed
- PyCharm available
- the repository was cloned successfully

## Official path

After cloning the repository, the standard local flow is:

```bash
make bootstrap
make db-init
make test
```

The manual steps below explain exactly what those commands are expected to achieve.

## 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
cd <repository_directory>
```

## 2. Create a virtual environment

```bash
python3.9 -m venv .venv
```

## 3. Activate the environment

```bash
source .venv/bin/activate
```

## 4. Upgrade pip and install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## 5. Configure environment variables

```bash
cp .env.example .env
```

Review `.env` and fill additional values only as the project evolves.

## 6. Create local state directories

These folders are intentionally local and should not be committed.

```bash
mkdir -p data_lake/bronze
mkdir -p data_lake/silver
mkdir -p data_lake/gold
mkdir -p state/sqlite
mkdir -p state/duckdb
mkdir -p artifacts
```

## 7. Initialize local databases

Preferred path:

```bash
make db-init
```

Manual equivalent:

```bash
sqlite3 state/sqlite/control_plane.db ".databases"
duckdb state/duckdb/serving.duckdb -c "SELECT 1;"
```

If the DuckDB CLI is not installed, the Python package is enough; the file can be created from Python later.

## 8. Open the project in PyCharm

- Open the repository root
- Configure the interpreter to `.venv/bin/python`
- Enable pytest as the default test runner
- Confirm the project root is the working directory for run configurations

## 9. Validate the environment

```bash
make test
```

Optional but recommended:

```bash
make lint
make format
```

## Completion criteria

Bootstrap is complete when:

- virtual environment exists
- dependencies install successfully
- PyCharm recognizes the interpreter
- tests run
- local state folders exist
- SQLite file exists or can be created
- DuckDB serving file exists or can be created

## Local state policy

Do not commit:

- `data_lake/`
- `state/`
- `artifacts/`
- `*.db`
- `*.duckdb`

The repository stores the recipe. The machine reconstructs the state.

## Pre-Setup Completion Gate

Before declaring the repository ready for controlled implementation, run:

`python -m quant_macro_os.bootstrap.pre_setup_completion_cli`

The completion gate validates operational readiness plus routed executive/VP knowledge coverage.
