def structured_log(event: str, **kwargs):
    return {"event": event, **kwargs}
