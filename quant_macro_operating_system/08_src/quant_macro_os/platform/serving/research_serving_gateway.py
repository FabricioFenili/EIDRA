class ResearchServingGateway:
    def serve_dataset(self, dataset_name: str, consumer: str):
        return {"status": "ok", "dataset_name": dataset_name, "consumer": consumer}
