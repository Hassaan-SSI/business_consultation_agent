from app.agents.registry import ALL_ASPECTS, downstream_of
from app.config import settings
from app.schemas.review import Critique
from app.schemas.state import PlannerState


def critic_node(state: PlannerState) -> dict:
    critiques = list(state.get("critiques") or [])
    iteration = state.get("review_iteration", 0)
    new_items: list[Critique] = []

    if settings.critic_debug_trigger and iteration == 0:
        new_items.append(
            Critique(
                id="critic:price_mismatch",
                target_aspect="financial",
                issue="Financial model price may exceed market willingness to pay (debug stub).",
                related_aspects=["market", "financial"],
                resolved=False,
            )
        )

    analyses = state.get("analyses") or {}
    market = analyses.get("market")
    financial = analyses.get("financial")
    if market and financial:
        m_metrics = market.metrics if hasattr(market, "metrics") else {}
        f_metrics = financial.metrics if hasattr(financial, "metrics") else {}
        high = m_metrics.get("suggested_price_high")
        price_used = f_metrics.get("price_used")
        if high is not None and price_used is not None and float(price_used) > float(high) + 0.01:
            new_items.append(
                Critique(
                    id="critic:price_above_market",
                    target_aspect="financial",
                    issue="Financial price assumption is above market suggested high.",
                    related_aspects=["market", "financial"],
                    resolved=False,
                )
            )

    merged = {c.id: c for c in critiques}
    for item in new_items:
        merged[item.id] = item
    all_critiques = list(merged.values())
    unresolved = [c for c in all_critiques if not c.resolved]

    update: dict = {"critiques": list(new_items)}
    if unresolved:
        targets = {c.target_aspect for c in unresolved}
        expanded: set[str] = set()
        for target in targets:
            expanded.add(target)
            expanded.update(downstream_of(target))
        update["rerun_aspects"] = sorted(expanded)
        update["review_iteration"] = iteration + 1
    else:
        update["rerun_aspects"] = []
    return update
