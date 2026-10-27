from app.agents.base import build_agent_graph, make_assumption, make_risk, stub_analysis
from app.agents.market.spec import SPEC
from app.schemas.state import PlannerState


def analyze(state: PlannerState) -> dict:
    idea = state.get("idea")
    title = idea.title if idea else "the venture"
    analysis = stub_analysis(
        aspect="market",
        summary=f"Stub market view for {title}: viable niche with competitive pressure.",
        findings=[
            "Urban specialty beverage demand is steady",
            "Three direct competitors identified (stub)",
            "Suggested price band $4.50–$8.00 per unit",
        ],
        metrics={
            "tam_usd": 1_500_000_000,
            "sam_usd": 30_000_000,
            "som_usd": 300_000,
            "suggested_price_low": 4.5,
            "suggested_price_mid": 6.0,
            "suggested_price_high": 8.0,
            "competitors": ["Competitor A", "Competitor B", "Competitor C"],
        },
        score=7.0,
    )
    return {
        "analyses": {"market": analysis},
        "assumptions": [
            make_assumption("market", "price_mid", "Mid-market price point", 6.0),
        ],
        "risks": [
            make_risk("market", "competition", "Incumbents may compress margins", 3, 4),
        ],
    }


def build_graph():
    return build_agent_graph(SPEC, analyze)
