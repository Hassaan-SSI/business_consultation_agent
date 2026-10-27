"""Placeholder RAG retriever for compliance agent (phase 3)."""


def retrieve_regulations(jurisdiction: str, query: str, k: int = 5) -> list[dict]:
    return [
        {
            "source": f"{jurisdiction} regulations (stub)",
            "snippet": f"Placeholder result for: {query}",
            "url": None,
        }
    ]
