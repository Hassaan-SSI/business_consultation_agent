import json
from pathlib import Path


def load_input(path: str | Path) -> tuple[str, dict]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(p)

    if p.suffix.lower() == ".txt":
        return p.read_text(encoding="utf-8"), {}

    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, str):
        return data, {}
    free_text = data.get("free_text") or ""
    questionnaire = data.get("questionnaire") or {}
    return free_text, questionnaire
