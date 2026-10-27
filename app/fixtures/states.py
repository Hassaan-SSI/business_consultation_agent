from app.fixtures.analyses import compliance_analysis, market_analysis, technical_analysis
from app.fixtures.ideas import coffee_shop_idea


def post_intake_state() -> dict:
    return {
        "idea": coffee_shop_idea(),
        "missing_fields": [],
        "analyses": {},
        "assumptions": [],
        "risks": [],
        "open_questions": [],
        "critiques": [],
        "rerun_aspects": ["market", "technical", "compliance", "financial", "operations"],
        "review_iteration": 0,
    }


def post_wave1_state() -> dict:
    state = post_intake_state()
    state["analyses"] = {
        "market": market_analysis(),
        "technical": technical_analysis(),
        "compliance": compliance_analysis(),
    }
    return state
