from pathlib import Path
from quant_macro_os.bootstrap.system_bootstrap_pipeline import bootstrap

def test_bootstrap_creates_database(tmp_path: Path):
    db_path = tmp_path / "test_bootstrap.db"
    result = bootstrap(db_path)
    assert result.exists()
