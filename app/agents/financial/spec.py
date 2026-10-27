from app.agents.base import AgentSpec

SPEC = AgentSpec(
    name="financial",
    aspect="financial",
    description="Unit economics, break-even, and runway (decision support).",
    depends_on=["market", "technical"],
    reads=["idea", "analyses.market", "analyses.technical"],
    writes=["analyses.financial", "assumptions", "risks"],
)
