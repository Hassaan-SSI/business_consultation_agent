from __future__ import annotations

from app.agents.compliance.spec import SPEC as COMPLIANCE_SPEC
from app.agents.financial.spec import SPEC as FINANCIAL_SPEC
from app.agents.market.spec import SPEC as MARKET_SPEC
from app.agents.operations.spec import SPEC as OPERATIONS_SPEC
from app.agents.technical.spec import SPEC as TECHNICAL_SPEC
from app.agents.base import AgentSpec

AGENTS: dict[str, AgentSpec] = {
    "market": MARKET_SPEC,
    "technical": TECHNICAL_SPEC,
    "compliance": COMPLIANCE_SPEC,
    "financial": FINANCIAL_SPEC,
    "operations": OPERATIONS_SPEC,
}

ALL_ASPECTS: list[str] = list(AGENTS.keys())

WAVE_1 = ["market", "technical", "compliance"]
WAVE_2 = ["financial"]
WAVE_3 = ["operations"]


def compute_waves() -> list[list[str]]:
    return [WAVE_1, WAVE_2, WAVE_3]


def downstream_of(aspect: str) -> list[str]:
    dependents: set[str] = set()
    changed = True
    frontier = {aspect}
    while changed:
        changed = False
        for name, spec in AGENTS.items():
            if name in dependents or name in frontier:
                continue
            if any(dep in frontier or dep in dependents for dep in spec.depends_on):
                dependents.add(name)
                changed = True
        frontier = dependents.copy()
    return sorted(dependents)
