from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from langgraph.graph import END, START, StateGraph

from app.schemas.analysis import AspectAnalysis
from app.schemas.risks import Assumption, OpenQuestion, Risk
from app.schemas.state import PlannerState


@dataclass
class AgentSpec:
    name: str
    aspect: str
    description: str
    depends_on: list[str] = field(default_factory=list)
    reads: list[str] = field(default_factory=list)
    writes: list[str] = field(default_factory=list)


AnalyzeFn = Callable[[PlannerState], dict[str, Any]]


def build_agent_graph(spec: AgentSpec, analyze_fn: AnalyzeFn):
    graph = StateGraph(PlannerState)
    graph.add_node(spec.aspect, analyze_fn)
    graph.add_edge(START, spec.aspect)
    graph.add_edge(spec.aspect, END)
    return graph.compile()


def make_assumption(aspect: str, slug: str, statement: str, value: Any = None) -> Assumption:
    return Assumption(
        id=f"{aspect}:{slug}",
        aspect=aspect,
        statement=statement,
        value=value,
        source="agent",
        confidence=0.6,
    )


def make_risk(
    aspect: str,
    slug: str,
    description: str,
    severity: int = 3,
    likelihood: int = 3,
    mitigation: str | None = None,
) -> Risk:
    return Risk(
        id=f"{aspect}:{slug}",
        aspect=aspect,
        description=description,
        severity=severity,
        likelihood=likelihood,
        mitigation=mitigation,
    )


def make_open_question(aspect: str, slug: str, question: str, blocking: bool = False) -> OpenQuestion:
    return OpenQuestion(
        id=f"{aspect}:{slug}",
        aspect=aspect,
        question=question,
        blocking=blocking,
    )


def stub_analysis(aspect: str, summary: str, findings: list[str], metrics: dict, score: float) -> AspectAnalysis:
    return AspectAnalysis(
        aspect=aspect,
        summary=summary,
        findings=findings,
        metrics=metrics,
        score=score,
        confidence=0.6,
        status="stub",
    )
