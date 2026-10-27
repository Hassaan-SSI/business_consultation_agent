from app.agents.registry import ALL_ASPECTS, compute_waves, downstream_of
from app.testing import check, exit_with_status


def main() -> None:
    waves = compute_waves()
    check(len(waves) == 3, "three waves")
    check("financial" in downstream_of("market"), "market downstream includes financial")
    check("operations" in downstream_of("financial"), "financial downstream includes operations")
    check(len(ALL_ASPECTS) == 5, "five specialist aspects")
    exit_with_status()


if __name__ == "__main__":
    main()
