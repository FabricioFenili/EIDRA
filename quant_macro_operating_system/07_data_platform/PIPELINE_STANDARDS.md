# PIPELINE STANDARDS

## Mandatory pipeline flow

```text
Extract -> Validate -> Transform -> Load -> Verify
```

## Design rules

- every pipeline must be idempotent
- every pipeline must log start, end, status, and records processed
- every pipeline must validate schema before promotion
- every pipeline must be safe to re-run

## Standard code structure

```text
pipelines/<source>/
  extract.py
  validate.py
  transform.py
  load.py
  pipeline.py
```

## Output rules

- bronze writes raw parquet
- silver writes standardized parquet
- gold writes analytics-ready parquet

## Control plane logging

Each execution should register in SQLite:
- `pipeline_name`
- `execution_start`
- `execution_end`
- `status`
- `records_processed`
- `notes` or `error_message` when applicable
