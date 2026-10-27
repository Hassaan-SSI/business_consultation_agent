from app.fixtures.states import post_wave1_state
from app.agents.financial.graph import analyze as financial_analyze
from app.nodes.synthesizer import synthesizer_node
from app.testing import check, exit_with_status


def main() -> None:
    state = post_wave1_state()
    state.update(financial_analyze(state))
    out = synthesizer_node(state)
    report = out.get("report")
    check(report is not None and report.markdown, "markdown report")
    check(report.recommendation in {"go", "no_go", "pivot"}, "valid recommendation")
    exit_with_status()


if __name__ == "__main__":
    main()
