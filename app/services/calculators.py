"""Placeholder deterministic finance calculators (phase 2)."""


def break_even_months(
    fixed_costs: float, price: float, variable_cost: float, units_per_month: float
) -> float | None:
    margin = price - variable_cost
    if margin <= 0 or units_per_month <= 0:
        return None
    monthly_contribution = margin * units_per_month
    if monthly_contribution <= 0:
        return None
    return fixed_costs / monthly_contribution


def runway_months(budget: float, monthly_burn: float) -> float | None:
    if monthly_burn <= 0:
        return None
    return budget / monthly_burn
