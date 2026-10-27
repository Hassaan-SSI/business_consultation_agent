from app import config
from app.agents.financial.graph import analyze as financial_analyze
from app.fixtures.states import post_wave1_state
from app.nodes.critic import critic_node
from app.nodes.routers import route_after_critic
from app.testing import check, exit_with_status


def main() -> None:
    config.settings.critic_debug_trigger = True
    state = post_wave1_state()
    state.update(financial_analyze(state))
    out = critic_node(state)
    state.update(out)
    route = route_after_critic(state)
    check(route == "wave1_router", "loops back when critiques unresolved")
    config.settings.critic_debug_trigger = False
    exit_with_status()


if __name__ == "__main__":
    main()
