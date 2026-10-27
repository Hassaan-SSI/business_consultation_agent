from app.agents.base import build_agent_graph, make_open_question, make_risk, stub_analysis
from app.agents.compliance.spec import SPEC
from app.schemas.analysis import Citation
from app.schemas.state import PlannerState


def analyze(state: PlannerState) -> dict:
    idea = state.get("idea")
    location = idea.location if idea else "Unknown"
    analysis = stub_analysis(
        aspect="compliance",
        summary=f"Stub compliance review for {location}.",
        findings=[
            "Business registration required",
            "Food-service permits likely required (stub)",
            "Sales tax registration needed",
        ],
        metrics={"license_count_estimate": 3},
        score=6.5,
    )
    analysis.citations = [
        Citation(source="stub regulation index", snippet=f"Obligations for {location}")
    ]
    return {
        "analyses": {"compliance": analysis},
        "risks": [
            make_risk("compliance", "permits", "Permit delays could push opening date", 3, 3),
        ],
        "open_questions": [
            make_open_question(
                "compliance",
                "zoning",
                "Confirm zoning allows food service at chosen site",
                blocking=False,
            ),
        ],
    }


def build_graph():
    return build_agent_graph(SPEC, analyze)
