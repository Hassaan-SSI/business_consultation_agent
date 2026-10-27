from app.agents.base import AgentSpec

SPEC = AgentSpec(
    name="market",
    aspect="market",
    description="Customer segments, market size, competitors, and pricing benchmarks.",
    depends_on=[],
    reads=["idea"],
    writes=["analyses.market", "assumptions", "risks", "open_questions"],
)
