from app.nodes.intake import intake_node
from app.testing import check, exit_with_status


def main() -> None:
    state = {
        "raw_input": "Coffee shop for students.",
        "questionnaire": {
            "target_customer": "Students",
            "problem": "No good coffee",
            "revenue_model": "Sales",
            "location": "Austin, TX",
        },
    }
    out = intake_node(state)
    check(out.get("idea") is not None, "idea extracted")
    check(out.get("missing_fields") == [], "no missing when questionnaire complete")
    exit_with_status()


if __name__ == "__main__":
    main()
