from app.agents.financial.graph import build_graph
from app.agents.market.graph import analyze as market_analyze
from app.fixtures.states import post_intake_state
from app.testing import check, exit_with_status


def main() -> None:
    state = post_intake_state()
    state.update(market_analyze(state))
    result = build_graph().invoke(state)
    metrics = result["analyses"]["financial"].metrics
    check(metrics.get("price_used") == 6.0, "financial reads market price")
    exit_with_status()


if __name__ == "__main__":
    main()
