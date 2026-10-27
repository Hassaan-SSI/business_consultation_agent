from pathlib import Path

from app.fileio.loader import load_input
from app.testing import check, exit_with_status


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    raw, q = load_input(root / "inputs/example_coffee_shop.json")
    check("coffee" in raw.lower(), "loads free text")
    check(q.get("title") == "Neighborhood Roast", "loads questionnaire")
    txt, q2 = load_input(root / "inputs/example_saas.txt")
    check("SaaS" in txt and q2 == {}, "txt mode")
    exit_with_status()


if __name__ == "__main__":
    main()
