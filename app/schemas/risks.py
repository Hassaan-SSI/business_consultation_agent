from typing import Any, Literal

from pydantic import BaseModel, Field


class Assumption(BaseModel):
    id: str
    aspect: str
    statement: str
    value: Any = None
    source: Literal["user", "agent", "derived"] = "agent"
    confidence: float = 0.7


class Risk(BaseModel):
    id: str
    aspect: str
    description: str
    severity: int = Field(ge=1, le=5)
    likelihood: int = Field(ge=1, le=5)
    mitigation: str | None = None


class OpenQuestion(BaseModel):
    id: str
    aspect: str
    question: str
    blocking: bool = False
