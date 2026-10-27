from app.agents.operations.graph import build_graph
from app.fixtures.states import post_wave1_state
from app.agents.financial.graph import analyze as financial_analyze
from app.testing import check, exit_with_status, print_agent_result


def main() -> None:
    state = post_wave1_state()
    state.update(financial_analyze(state))
    result = build_graph().invoke(state)
    print_agent_result("operations", result)
    check(len(result["analyses"]["operations"].metrics.get("channels", [])) >= 1, "channels listed")
    exit_with_status()


if __name__ == "__main__":
    main()
