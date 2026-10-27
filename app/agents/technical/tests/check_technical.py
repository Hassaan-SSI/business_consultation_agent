from app.agents.technical.graph import build_graph
from app.fixtures.states import post_intake_state
from app.testing import check, exit_with_status, print_agent_result


def main() -> None:
    result = build_graph().invoke(post_intake_state())
    print_agent_result("technical", result)
    analysis = result["analyses"]["technical"]
    check("mvp_cost_usd" in analysis.metrics, "mvp cost present")
    exit_with_status()


if __name__ == "__main__":
    main()
