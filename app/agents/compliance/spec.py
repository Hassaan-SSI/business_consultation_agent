from app.agents.base import AgentSpec

SPEC = AgentSpec(
    name="compliance",
    aspect="compliance",
    description="Regulations, licenses, and data/IP concerns for the jurisdiction.",
    depends_on=[],
    reads=["idea"],
    writes=["analyses.compliance", "assumptions", "risks", "open_questions"],
)
