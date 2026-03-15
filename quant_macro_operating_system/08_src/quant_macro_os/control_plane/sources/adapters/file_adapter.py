from pathlib import Path

class FileAdapter:
    def fetch(self, config):
        path = Path(str(config.get("path", "")))
        return {
            "source_type": "file",
            "path": str(path),
            "content": path.read_text(encoding="utf-8") if path.exists() else "",
            "metadata": {"exists": path.exists()},
        }
