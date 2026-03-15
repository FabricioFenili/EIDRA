from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable

DB_PATH = Path("quant_macro_os.db")

TABLE_STATEMENTS: Iterable[str] = (
    '''
    CREATE TABLE IF NOT EXISTS metadata_datasets (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        source TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS metadata_features (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        description TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS metadata_pipelines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS research_experiments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        params_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS monitoring_system_runs (
        id INTEGER PRIMARY KEY,
        run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL
    )
    '''
)

def create_database(db_path: Path = DB_PATH) -> sqlite3.Connection:
    return sqlite3.connect(db_path)

def create_metadata_tables(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    for statement in TABLE_STATEMENTS:
        cursor.execute(statement)
    conn.commit()

def bootstrap(db_path: Path = DB_PATH) -> Path:
    conn = create_database(db_path)
    try:
        create_metadata_tables(conn)
    finally:
        conn.close()
    return db_path

if __name__ == "__main__":
    result = bootstrap()
    print(f"System bootstrap completed: {result}")
