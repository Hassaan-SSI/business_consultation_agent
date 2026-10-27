from typing import Annotated, Any, TypedDict

from app.schemas.analysis import AspectAnalysis
from app.schemas.idea import BusinessIdea
from app.schemas.reducers import merge_by_id, merge_dict
from app.schemas.review import Critique, Report
from app.schemas.risks import Assumption, OpenQuestion, Risk


class PlannerState(TypedDict, total=False):
    raw_input: str
    questionnaire: dict[str, Any]
    idea: BusinessIdea
    missing_fields: list[str]
    analyses: Annotated[dict[str, AspectAnalysis], merge_dict]
    assumptions: Annotated[list[Assumption], merge_by_id]
    risks: Annotated[list[Risk], merge_by_id]
    open_questions: Annotated[list[OpenQuestion], merge_by_id]
    critiques: Annotated[list[Critique], merge_by_id]
    rerun_aspects: list[str]
    review_iteration: int
    report: Report
