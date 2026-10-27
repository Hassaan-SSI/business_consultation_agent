from __future__ import annotations

import argparse
import uuid

from langgraph.types import Command

from app.agents.registry import ALL_ASPECTS
from app.fileio.exporter import export_report_markdown
from app.fileio.loader import load_input
from app.graph import build_graph


def _prompt_missing_fields(missing: list[str]) -> dict:
    patch: dict = {}
    for field in missing:
        value = input(f"Enter {field}: ").strip()
        if value:
            patch[field] = value
    return patch


def run_with_interrupts(initial_state: dict) -> dict:
    app = build_graph()
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    app.invoke(initial_state, config)

    while True:
        snapshot = app.get_state(config)
        if not snapshot.next:
            break
        interrupt_values = []
        for task in snapshot.tasks:
            interrupt_values.extend(task.interrupts)
        if not interrupt_values:
            break
        payload = interrupt_values[0].value
        missing = payload.get("missing_fields", []) if isinstance(payload, dict) else []
        patch = _prompt_missing_fields(missing)
        app.invoke(Command(resume=patch), config)

    final = app.get_state(config)
    return final.values


def main() -> None:
    parser = argparse.ArgumentParser(description="Business idea multi-agent planner")
    parser.add_argument("--input", required=True, help="Path to JSON or TXT input file")
    args = parser.parse_args()

    raw_input, questionnaire = load_input(args.input)
    initial_state = {
        "raw_input": raw_input,
        "questionnaire": questionnaire,
        "analyses": {},
        "assumptions": [],
        "risks": [],
        "open_questions": [],
        "critiques": [],
        "rerun_aspects": ALL_ASPECTS,
        "review_iteration": 0,
    }

    print("Running planner graph...")
    result = run_with_interrupts(initial_state)
    report = result.get("report")
    if report is None:
        print("No report produced.")
        return

    idea = result.get("idea")
    title = idea.title if idea and idea.title else "business-plan"
    path = export_report_markdown(report, title=title)
    print(f"Recommendation: {report.recommendation}")
    print(f"Report written to: {path}")


if __name__ == "__main__":
    main()
