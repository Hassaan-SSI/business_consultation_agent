import os
from pathlib import Path

from app.cli import run_with_interrupts
from app.agents.registry import ALL_ASPECTS
from app.fileio.loader import load_input
from app.testing import check, exit_with_status


def main() -> None:
    os.environ["LLM_MODE"] = "mock"
    root = Path(__file__).resolve().parents[2]
    raw, questionnaire = load_input(root / "inputs/example_coffee_shop.json")
    initial = {
        "raw_input": raw,
        "questionnaire": questionnaire,
        "analyses": {},
        "assumptions": [],
        "risks": [],
        "open_questions": [],
        "critiques": [],
        "rerun_aspects": ALL_ASPECTS,
        "review_iteration": 0,
    }
    result = run_with_interrupts(initial)
    report = result.get("report")
    check(report is not None, "report created")
    check(len(report.scorecard) >= 5, "all aspects scored")
    exit_with_status()


if __name__ == "__main__":
    main()
