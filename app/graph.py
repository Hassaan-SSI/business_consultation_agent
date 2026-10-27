"""Parent graph wiring only — no business logic."""

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from app.agents.compliance.graph import analyze as compliance_analyze
from app.agents.financial.graph import analyze as financial_analyze
from app.agents.market.graph import analyze as market_analyze
from app.agents.operations.graph import analyze as operations_analyze
from app.agents.technical.graph import analyze as technical_analyze
from app.nodes.critic import critic_node
from app.nodes.intake import intake_node
from app.nodes.joins import wave1_join, wave2_join
from app.nodes.routers import route_after_critic, route_wave_1, route_wave_2, route_wave_3
from app.nodes.synthesizer import synthesizer_node
from app.schemas.state import PlannerState

WAVE1_TARGETS = ["market", "technical", "compliance", "wave1_join"]


def _wave1_router_passthrough(state: PlannerState) -> dict:
    return {}


def build_graph(checkpointer=None):
    graph = StateGraph(PlannerState)

    graph.add_node("intake", intake_node)
    graph.add_node("wave1_router", _wave1_router_passthrough)
    graph.add_node("market", market_analyze)
    graph.add_node("technical", technical_analyze)
    graph.add_node("compliance", compliance_analyze)
    graph.add_node("wave1_join", wave1_join)
    graph.add_node("financial", financial_analyze)
    graph.add_node("wave2_join", wave2_join)
    graph.add_node("operations", operations_analyze)
    graph.add_node("critic", critic_node)
    graph.add_node("synthesizer", synthesizer_node)

    graph.add_edge(START, "intake")
    graph.add_edge("intake", "wave1_router")
    graph.add_conditional_edges("wave1_router", route_wave_1, WAVE1_TARGETS)
    graph.add_edge("market", "wave1_join")
    graph.add_edge("technical", "wave1_join")
    graph.add_edge("compliance", "wave1_join")
    graph.add_conditional_edges("wave1_join", route_wave_2, ["financial", "wave2_join"])
    graph.add_edge("financial", "wave2_join")
    graph.add_conditional_edges("wave2_join", route_wave_3, ["operations", "critic"])
    graph.add_edge("operations", "critic")
    graph.add_conditional_edges("critic", route_after_critic, ["wave1_router", "synthesizer"])
    graph.add_edge("synthesizer", END)

    memory = checkpointer if checkpointer is not None else MemorySaver()
    return graph.compile(checkpointer=memory)
