from app.schemas.review import Report
from app.schemas.risks import Risk
from app.schemas.state import PlannerState


def _risk_score(risk: Risk) -> int:
    return risk.severity * risk.likelihood


def synthesizer_node(state: PlannerState) -> dict:
    analyses = state.get("analyses") or {}
    scorecard = {
        aspect: float(analysis.score)
        for aspect, analysis in analyses.items()
        if hasattr(analysis, "score")
    }
    avg = sum(scorecard.values()) / len(scorecard) if scorecard else 0.0
    if avg >= 7.5:
        recommendation = "go"
    elif avg >= 5.5:
        recommendation = "pivot"
    else:
        recommendation = "no_go"

    risks = list(state.get("risks") or [])
    top_risks = sorted(risks, key=_risk_score, reverse=True)[:5]

    idea = state.get("idea")
    title = idea.title if idea and idea.title else "Business Idea"

    lines = [
        f"# {title} - Decision Support Report",
        "",
        "> Decision support with stated assumptions, not predictions.",
        "",
        f"**Recommendation:** `{recommendation}`",
        "",
        "## Scorecard",
    ]
    for aspect, score in sorted(scorecard.items()):
        lines.append(f"- **{aspect}**: {score:.1f} / 10")
    lines.extend(["", "## Top risks"])
    for risk in top_risks:
        lines.append(
            f"- ({risk.aspect}) {risk.description} [S{risk.severity} L{risk.likelihood}]"
        )
    lines.extend(
        [
            "",
            "## Next steps",
            "- Validate top assumptions with customer interviews",
            "- Re-run financial model after pricing experiments",
            "- Confirm compliance checklist for your jurisdiction",
        ]
    )
    assumptions = state.get("assumptions") or []
    if assumptions:
        lines.extend(["", "## Assumptions (sample)"])
        for assumption in assumptions[:8]:
            lines.append(f"- ({assumption.aspect}) {assumption.statement}: {assumption.value}")

    report = Report(
        scorecard=scorecard,
        recommendation=recommendation,
        top_risks=top_risks,
        next_steps=[
            "Validate top assumptions with customers",
            "Stress-test pricing and unit economics",
            "Complete compliance checklist",
        ],
        markdown="\n".join(lines) + "\n",
    )
    return {"report": report}
