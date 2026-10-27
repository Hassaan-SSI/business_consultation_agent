from app.agents.compliance.graph import build_graph
from app.fixtures.states import post_intake_state
from app.testing import check, exit_with_status, print_agent_result


def main() -> None:
    result = build_graph().invoke(post_intake_state())
    print_agent_result("compliance", result)
    analysis = result["analyses"]["compliance"]
    check(len(analysis.citations) >= 1, "has citations")
    exit_with_status()


if __name__ == "__main__":
    main()
