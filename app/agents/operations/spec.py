from app.agents.base import AgentSpec

SPEC = AgentSpec(
    name="operations",
    aspect="operations",
    description="Go-to-market channels, milestones, and operational setup.",
    depends_on=["market", "technical", "compliance", "financial"],
    reads=["idea", "analyses"],
    writes=["analyses.operations", "assumptions", "risks", "open_questions"],
)
