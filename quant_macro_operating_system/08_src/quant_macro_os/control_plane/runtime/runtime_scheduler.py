from __future__ import annotations
from datetime import date

from quant_macro_os.control_plane.runtime.source_instance_registry import SourceInstanceRegistry
from quant_macro_os.control_plane.governance.schedule_policy_registry import SchedulePolicyRegistry
from quant_macro_os.control_plane.services.execution_eligibility_engine import ExecutionEligibilityEngine

class RuntimeScheduler:
    def __init__(self, db_path=None, repo_root=None):
        self.instances = SourceInstanceRegistry(db_path=db_path, repo_root=repo_root)
        self.schedules = SchedulePolicyRegistry(db_path=db_path, repo_root=repo_root)
        self.eligibility = ExecutionEligibilityEngine()

    def plan_for_date(self, year: int, month: int, day: int):
        today = date(year, month, day)
        schedule_map = {row["policy_name"]: row for row in self.schedules.list_all()}
        plan = []
        for row in self.instances.list_all():
            if int(row["is_enabled"]) != 1:
                continue
            schedule = schedule_map.get(row["schedule_policy_name"])
            if not schedule:
                continue
            should_run = self.eligibility.should_run(schedule["update_frequency"], today)
            if should_run:
                plan.append({
                    "instance_name": row["instance_name"],
                    "source_name": row["source_name"],
                    "pipeline_name": row["pipeline_name"],
                    "data_family": row["data_family"],
                    "publish_target_name": row["publish_target_name"],
                    "schedule_policy_name": row["schedule_policy_name"],
                    "update_frequency": schedule["update_frequency"],
                })
        return plan
