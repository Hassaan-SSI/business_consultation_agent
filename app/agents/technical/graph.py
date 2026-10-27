from app.agents.base import build_agent_graph, make_assumption, make_risk, stub_analysis
from app.agents.technical.spec import SPEC
from app.schemas.state import PlannerState


def analyze(state: PlannerState) -> dict:
    idea = state.get("idea")
    title = idea.title if idea else "the venture"
    analysis = stub_analysis(
        aspect="technical",
        summary=f"Stub technical plan for {title}: moderate complexity MVP.",
        findings=[
            "Use off-the-shelf POS and accounting tools",
            "Custom mobile app not required for MVP",
            "10-week build timeline (stub)",
        ],
        metrics={
            "stack": ["Square POS", "QuickBooks", "Notion"],
            "complexity_score": 3,
            "mvp_cost_usd": 22000,
            "timeline_weeks": 10,
        },
        score=7.8,
    )
    return {
        "analyses": {"technical": analysis},
        "assumptions": [
            make_assumption("technical", "mvp_cost", "MVP build cost estimate (USD)", 22000),
        ],
        "risks": [
            make_risk("technical", "vendor_lock", "POS vendor dependency", 2, 3),
        ],
    }


def build_graph():
    return build_agent_graph(SPEC, analyze)
