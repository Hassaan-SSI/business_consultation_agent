from langgraph.types import Send

from app.agents.registry import ALL_ASPECTS, WAVE_1, WAVE_2, WAVE_3
from app.config import settings
from app.schemas.state import PlannerState


def _aspects_to_run(state: PlannerState) -> set[str]:
    return set(state.get("rerun_aspects") or ALL_ASPECTS)


def route_wave_1(state: PlannerState):
    to_run = [a for a in WAVE_1 if a in _aspects_to_run(state)]
    if not to_run:
        return "wave1_join"
    return [Send(a, state) for a in to_run]


def route_wave_2(state: PlannerState):
    if "financial" in _aspects_to_run(state):
        return "financial"
    return "wave2_join"


def route_wave_3(state: PlannerState):
    if "operations" in _aspects_to_run(state):
        return "operations"
    return "critic"


def route_after_critic(state: PlannerState):
    critiques = state.get("critiques") or []
    unresolved = [c for c in critiques if not getattr(c, "resolved", False)]
    iteration = state.get("review_iteration", 0)
    if unresolved and iteration < settings.max_review_iterations:
        return "wave1_router"
    return "synthesizer"
