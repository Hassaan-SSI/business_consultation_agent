import os

from app.fixtures.states import post_wave1_state
from app.agents.financial.graph import analyze as financial_analyze
from app.nodes.critic import critic_node
from app.testing import check, exit_with_status


def main() -> None:
    os.environ["CRITIC_DEBUG_TRIGGER"] = "true"
    from app import config

    config.settings.critic_debug_trigger = True
    state = post_wave1_state()
    state.update(financial_analyze(state))
    out = critic_node(state)
    check(len(out.get("critiques", [])) >= 1, "critique emitted")
    check("financial" in (out.get("rerun_aspects") or []), "rerun targets financial")
    exit_with_status()


if __name__ == "__main__":
    main()
