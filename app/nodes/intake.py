from __future__ import annotations

from langchain_core.messages import HumanMessage
from langgraph.types import interrupt

from app.agents.registry import ALL_ASPECTS
from app.schemas.idea import REQUIRED_INTAKE_FIELDS, BusinessIdea
from app.schemas.state import PlannerState
from app.services.llm import get_llm


def _missing_fields(idea: BusinessIdea) -> list[str]:
    missing: list[str] = []
    for field in REQUIRED_INTAKE_FIELDS:
        if not getattr(idea, field, None):
            missing.append(field)
    return missing


def _merge_questionnaire(idea: BusinessIdea, questionnaire: dict) -> BusinessIdea:
    data = idea.model_dump()
    for key, value in questionnaire.items():
        if value is None or value == "" or value == []:
            continue
        data[key] = value
    return BusinessIdea(**data)


def _extract_idea(raw_input: str, questionnaire: dict, force_live: bool = False) -> BusinessIdea:
    llm = get_llm(force_live=force_live).with_structured_output(BusinessIdea)
    prompt = (
        "Extract a structured business idea from the user input. "
        "Use null for unknown fields.\n\n"
        f"Free text:\n{raw_input}\n\n"
        f"Questionnaire (may be partial):\n{questionnaire}"
    )
    extracted = llm.invoke([HumanMessage(content=prompt)])
    if isinstance(extracted, BusinessIdea):
        return _merge_questionnaire(extracted, questionnaire)
    return _merge_questionnaire(BusinessIdea.model_validate(extracted), questionnaire)


def intake_node(state: PlannerState) -> dict:
    raw_input = state.get("raw_input") or ""
    questionnaire = state.get("questionnaire") or {}
    idea = state.get("idea")
    if idea is None:
        idea = _extract_idea(raw_input, questionnaire)

    missing = _missing_fields(idea)
    while missing:
        user_patch = interrupt(
            {
                "type": "missing_fields",
                "missing_fields": missing,
                "message": "Please provide values for the missing fields.",
            }
        )
        if isinstance(user_patch, dict):
            questionnaire = {**questionnaire, **user_patch}
            idea = _merge_questionnaire(idea, user_patch)
        missing = _missing_fields(idea)

    rerun = state.get("rerun_aspects") or ALL_ASPECTS
    return {
        "idea": idea,
        "missing_fields": [],
        "rerun_aspects": rerun,
    }
