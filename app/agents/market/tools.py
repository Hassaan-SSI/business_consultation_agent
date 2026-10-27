from app.services.search import web_search


def competitor_scan(query: str) -> list[dict]:
    return web_search(f"competitors {query}")
