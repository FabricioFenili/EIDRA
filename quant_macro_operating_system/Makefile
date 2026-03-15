.PHONY: bootstrap install db-init test lint format check clean activate help

PYTHON ?= python3.9
VENV_DIR ?= .venv
VENV_PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
PYTEST := $(VENV_DIR)/bin/pytest
BLACK := $(VENV_DIR)/bin/black
ISORT := $(VENV_DIR)/bin/isort
FLAKE8 := $(VENV_DIR)/bin/flake8

help:
	@echo "Available commands:"
	@echo "  make bootstrap  - create venv, install dependencies, create local folders"
	@echo "  make install    - install dependencies into existing venv"
	@echo "  make db-init    - initialize local SQLite and DuckDB state files"
	@echo "  make test       - run pytest"
	@echo "  make lint       - run flake8"
	@echo "  make format     - run isort and black"
	@echo "  make check      - run lint and tests"
	@echo "  make clean      - remove caches and temporary files"
	@echo "  make activate   - print activation command"

bootstrap:
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e .
	mkdir -p data_lake/bronze data_lake/silver data_lake/gold
	mkdir -p state/sqlite state/duckdb artifacts

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

db-init:
	mkdir -p state/sqlite state/duckdb
	$(VENV_PYTHON) -c "from pathlib import Path; import sqlite3; sqlite_path = Path('state/sqlite/control_plane.db'); sqlite_path.parent.mkdir(parents=True, exist_ok=True); conn = sqlite3.connect(sqlite_path); conn.execute('CREATE TABLE IF NOT EXISTS system_bootstrap (created_at TEXT DEFAULT CURRENT_TIMESTAMP)'); conn.commit(); conn.close(); import duckdb; duck_path = Path('state/duckdb/serving.duckdb'); duck_path.parent.mkdir(parents=True, exist_ok=True); con = duckdb.connect(str(duck_path)); con.execute('CREATE TABLE IF NOT EXISTS system_bootstrap(created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'); con.close(); print('Initialized local SQLite and DuckDB state.')"

test:
	$(PYTEST) -q

lint:
	$(FLAKE8) 08_src 09_tests

format:
	$(ISORT) 08_src 09_tests
	$(BLACK) 08_src 09_tests

check: lint test

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache .mypy_cache

activate:
	@echo "source $(VENV_DIR)/bin/activate"
