from app.agents.base import build_agent_graph, make_assumption, make_risk, stub_analysis
from app.agents.financial.spec import SPEC
from app.schemas.state import PlannerState
from app.services.calculators import break_even_months, runway_months


def _get_metric(state: PlannerState, aspect: str, key: str, default: float) -> float:
    analyses = state.get("analyses") or {}
    analysis = analyses.get(aspect)
    if analysis is None:
        return default
    metrics = analysis.metrics if hasattr(analysis, "metrics") else {}
    value = metrics.get(key, default)
    return float(value)


def analyze(state: PlannerState) -> dict:
    idea = state.get("idea")
    price = _get_metric(state, "market", "suggested_price_mid", 6.0)
    mvp_cost = _get_metric(state, "technical", "mvp_cost_usd", 20000.0)
    budget = float(idea.budget) if idea and idea.budget else 50000.0
    variable_cost = 2.2
    units_per_month = 1200.0
    monthly_fixed = 8500.0
    be_months = break_even_months(mvp_cost + monthly_fixed * 6, price, variable_cost, units_per_month)
    runway = runway_months(budget, monthly_fixed + 2000)
    analysis = stub_analysis(
        aspect="financial",
        summary="Stub financial model using market price and technical MVP cost.",
        findings=[
            f"Uses market mid-price ${price:.2f} (stub)",
            f"MVP cost input ${mvp_cost:,.0f} from technical analysis",
            "Figures are illustrative, not predictions",
        ],
        metrics={
            "price_used": price,
            "mvp_cost_used": mvp_cost,
            "cac_usd": 18.0,
            "ltv_usd": 210.0,
            "gross_margin_pct": round((price - variable_cost) / price * 100, 1),
            "break_even_months": round(be_months, 1) if be_months else None,
            "runway_months": round(runway, 1) if runway else None,
        },
        score=6.8,
    )
    return {
        "analyses": {"financial": analysis},
        "assumptions": [
            make_assumption("financial", "units", "Monthly units sold at steady state", units_per_month),
            make_assumption("financial", "variable_cost", "Variable cost per unit", variable_cost),
        ],
        "risks": [
            make_risk("financial", "runway", "Runway may be tight if sales ramp slowly", 4, 3),
        ],
    }


def build_graph():
    return build_agent_graph(SPEC, analyze)
