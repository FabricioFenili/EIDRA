from pathlib import Path
from quant_macro_os.control_plane.services.repo_browser import RepoBrowser

class SystemStateService:
    def __init__(self, repo_root: Path, api):
        self.repo_root = repo_root.resolve()
        self.api = api

    def snapshot(self):
        files = RepoBrowser(self.repo_root).list_files()
        return {
            "tracked_files": len(files),
            "projects": len(self.api.list_projects()),
            "sources": len(self.api.list_sources()),
            "pipelines": len(self.api.list_pipelines()),
            "pipeline_runs": len(self.api.list_pipeline_runs()),
            "patches": len(self.api.list_patches()),
            "audit_events": len(self.api.get_audit_events()),
        }
