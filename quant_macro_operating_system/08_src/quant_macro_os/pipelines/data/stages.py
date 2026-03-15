class DataPipelineStages:
    def source(self, payload):
        return payload

    def ingest(self, payload):
        return payload

    def normalize(self, payload):
        return payload

    def validate(self, payload):
        return payload

    def curate(self, payload):
        return payload

    def publish(self, payload):
        return payload
