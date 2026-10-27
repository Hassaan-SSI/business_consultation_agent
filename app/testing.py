from __future__ import annotations

import sys
from typing import Any

_failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if condition:
        print(f"  PASS: {message}")
    else:
        print(f"  FAIL: {message}")
        _failures.append(message)


def print_agent_result(aspect: str, result: dict[str, Any]) -> None:
    print(f"\n=== {aspect} agent output ===")
    analyses = result.get("analyses") or {}
    analysis = analyses.get(aspect)
    if analysis is None:
        print("(no analysis)")
        return
    if hasattr(analysis, "model_dump"):
        analysis = analysis.model_dump()
    print(f"Summary: {analysis.get('summary')}")
    print(f"Score: {analysis.get('score')}  Confidence: {analysis.get('confidence')}")
    print("Findings:")
    for f in analysis.get("findings") or []:
        print(f"  - {f}")
    print("Metrics:", analysis.get("metrics"))
    print(
        f"Assumptions: {len(result.get('assumptions') or [])}  "
        f"Risks: {len(result.get('risks') or [])}"
    )


def exit_with_status() -> None:
    if _failures:
        print(f"\n{len(_failures)} check(s) failed.")
        sys.exit(1)
    print("\nAll checks passed.")
    sys.exit(0)
