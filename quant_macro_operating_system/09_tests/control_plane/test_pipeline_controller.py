from pathlib import Path

from quant_macro_os.control_plane.pipeline.pipeline_controller import PipelineController

def test_pipeline_controller_bootstrap_and_registry(tmp_path: Path):
    db_path = tmp_path / "control.db"
    controller = PipelineController(db_path=db_path, repo_root=tmp_path)
    db = tmp_path / "bootstrap.db"
    assert controller.run_bootstrap(db).exists()
    controller.save_pipeline("bacen_pipeline", "bacen_sgs", ["source", "ingest", "normalize", "publish"])
    rows = controller.list_pipelines()
    assert rows[0]["name"] == "bacen_pipeline"
    result = controller.run_pipeline("bacen_pipeline", {"series": "11"})
    assert result["status"] == "ok"
    assert result["steps_executed"] == ["source", "ingest", "normalize", "publish"]
