from typing import Any, Literal

from pydantic import BaseModel, Field


class TeamMember(BaseModel):
    name: str = ""
    role: str = ""
    skills: list[str] = Field(default_factory=list)


class BusinessIdea(BaseModel):
    title: str | None = None
    description: str | None = None
    target_customer: str | None = None
    problem: str | None = None
    solution: str | None = None
    revenue_model: str | None = None
    price_point: float | None = None
    currency: str = "USD"
    location: str | None = None
    budget: float | None = None
    team: list[TeamMember] = Field(default_factory=list)
    stage: Literal["idea", "prototype", "launched"] = "idea"
    extra: dict[str, Any] = Field(default_factory=dict)


REQUIRED_INTAKE_FIELDS = (
    "target_customer",
    "problem",
    "revenue_model",
    "location",
)
