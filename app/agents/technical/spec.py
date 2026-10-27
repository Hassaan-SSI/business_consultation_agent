from app.agents.base import AgentSpec

SPEC = AgentSpec(
    name="technical",
    aspect="technical",
    description="Stack, build complexity, MVP scope, cost and timeline.",
    depends_on=[],
    reads=["idea"],
    writes=["analyses.technical", "assumptions", "risks"],
)
