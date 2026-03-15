class HTMLAdapter:
    def fetch(self, config):
        return {
            "source_type": "html",
            "html": config.get("mock_html", "<table></table>"),
            "metadata": {"url": config.get("url", "")},
        }
