from langgraph.types import Send

from app.fixtures.states import post_intake_state
from app.nodes.routers import route_wave_1, route_wave_2
from app.testing import check, exit_with_status


def main() -> None:
    state = post_intake_state()
    wave1 = route_wave_1(state)
    check(isinstance(wave1, list) and all(isinstance(s, Send) for s in wave1), "wave1 sends")
    partial = dict(state)
    partial["rerun_aspects"] = ["financial"]
    wave2 = route_wave_2(partial)
    check(wave2 == "financial", "wave2 routes financial")
    exit_with_status()


if __name__ == "__main__":
    main()
