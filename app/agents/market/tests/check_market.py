from app.agents.market.graph import build_graph
from app.fixtures.states import post_intake_state
from app.testing import check, exit_with_status, print_agent_result


def main() -> None:
    result = build_graph().invoke(post_intake_state())
    print_agent_result("market", result)
    analysis = result["analyses"]["market"]
    check(analysis.aspect == "market", "aspect key")
    check(0 <= analysis.score <= 10, "score in range")
    check("suggested_price_mid" in analysis.metrics, "suggested price present")
    exit_with_status()


if __name__ == "__main__":
    main()
