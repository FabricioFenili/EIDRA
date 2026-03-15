from datetime import date
class ExecutionEligibilityEngine:
    def should_run(self, update_frequency: str, today: date) -> bool:
        weekday = today.weekday()
        if update_frequency == "daily":
            return True
        if update_frequency == "business_daily":
            return weekday < 5
        if update_frequency == "weekly":
            return weekday == 0
        if update_frequency == "monthly":
            return today.day == 1
        if update_frequency == "quarterly":
            return today.day == 1 and today.month in (1, 4, 7, 10)
        if update_frequency == "annual":
            return today.day == 1 and today.month == 1
        if update_frequency in {"event_driven", "on_demand"}:
            return False
        return False
