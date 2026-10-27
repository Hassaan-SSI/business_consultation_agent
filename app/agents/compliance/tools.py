from app.services.retriever import retrieve_regulations


def lookup_obligations(jurisdiction: str, topic: str) -> list[dict]:
    return retrieve_regulations(jurisdiction, topic)
