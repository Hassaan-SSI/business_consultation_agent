from typing import Any, Literal

from pydantic import BaseModel, Field


class Citation(BaseModel):
    source: str
    url: str | None = None
    snippet: str | None = None


class AspectAnalysis(BaseModel):
    aspect: str
    summary: str
    findings: list[str] = Field(default_factory=list)
    metrics: dict[str, Any] = Field(default_factory=dict)
    score: float = 0.0
    confidence: float = 0.5
    citations: list[Citation] = Field(default_factory=list)
    status: Literal["stub", "complete", "insufficient_evidence"] = "stub"
    iteration: int = 0
