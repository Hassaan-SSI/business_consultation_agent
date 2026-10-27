from app.agents.financial.graph import build_graph
from app.fixtures.states import post_wave1_state
from app.testing import check, exit_with_status, print_agent_result


def main() -> None:
    result = build_graph().invoke(post_wave1_state())
    print_agent_result("financial", result)
    metrics = result["analyses"]["financial"].metrics
    check("break_even_months" in metrics, "break-even computed")
    check(metrics.get("price_used") == 6.0, "uses market price from fixtures")
    exit_with_status()


if __name__ == "__main__":
    main()
