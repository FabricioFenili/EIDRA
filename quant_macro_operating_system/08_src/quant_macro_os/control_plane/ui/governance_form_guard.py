from __future__ import annotations

def registration_readiness(
    source_names: list[str],
    data_families: list[str],
    contracts: list[str],
    schedules: list[str],
    publish_targets: list[str],
    join_policies: list[str],
    pipelines: list[str],
) -> dict:
    requirements = {
        "sources": bool(source_names),
        "data_families": bool(data_families),
        "contracts": bool(contracts),
        "schedule_policies": bool(schedules),
        "publish_targets": bool(publish_targets),
        "join_key_policies": bool(join_policies),
        "pipelines": bool(pipelines),
    }
    missing = [key for key, ok in requirements.items() if not ok]
    return {"ready": not missing, "requirements": requirements, "missing": missing}
