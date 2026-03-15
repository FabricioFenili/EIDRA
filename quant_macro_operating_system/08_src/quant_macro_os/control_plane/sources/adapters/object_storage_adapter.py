class ObjectStorageAdapter:
    def fetch(self, config):
        return {
            "source_type": "object_storage",
            "bucket": config.get("bucket", ""),
            "key": config.get("key", ""),
            "content": config.get("mock_content", ""),
            "metadata": {},
        }
