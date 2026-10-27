from typing import Literal

from pydantic import BaseModel, Field

from app.schemas.risks import Risk


class Critique(BaseModel):
    id: str
    target_aspect: str
    issue: str
    related_aspects: list[str] = Field(default_factory=list)
    resolved: bool = False


class Report(BaseModel):
    scorecard: dict[str, float] = Field(default_factory=dict)
    recommendation: Literal["go", "no_go", "pivot"] = "pivot"
    top_risks: list[Risk] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)
    markdown: str = ""
