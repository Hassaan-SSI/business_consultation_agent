from app.agents.base import build_agent_graph, make_open_question, make_risk, stub_analysis
from app.agents.operations.spec import SPEC
from app.schemas.state import PlannerState
from app.agents.operations.tools import default_channels


def analyze(state: PlannerState) -> dict:
    idea = state.get("idea")
    title = idea.title if idea else "the venture"
    analysis = stub_analysis(
        aspect="operations",
        summary=f"Stub GTM and operations plan for {title}.",
        findings=[
            "Focus on high-traffic morning commute window",
            "Hire 2 baristas for launch",
            "90-day milestone plan (stub)",
        ],
        metrics={
            "channels": default_channels(),
            "milestones_90d": [
                "Secure lease and permits",
                "Hire and train staff",
                "Soft launch with loyalty program",
            ],
            "team_gaps": ["Part-time accountant"],
        },
        score=7.4,
    )
    return {
        "analyses": {"operations": analysis},
        "risks": [
            make_risk("operations", "staffing", "Barista hiring market is tight", 3, 3),
        ],
        "open_questions": [
            make_open_question("operations", "hours", "Confirm optimal opening hours", blocking=False),
        ],
    }


def build_graph():
    return build_agent_graph(SPEC, analyze)
