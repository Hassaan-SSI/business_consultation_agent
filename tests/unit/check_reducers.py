from app.schemas.reducers import merge_by_id, merge_dict
from app.schemas.risks import Risk
from app.testing import check, exit_with_status


def main() -> None:
    merged = merge_dict({"a": 1}, {"b": 2})
    check(merged == {"a": 1, "b": 2}, "merge_dict")
    left = [Risk(id="r1", aspect="market", description="x", severity=1, likelihood=1)]
    right = [Risk(id="r1", aspect="market", description="y", severity=2, likelihood=2)]
    out = merge_by_id(left, right)
    check(len(out) == 1 and out[0].description == "y", "merge_by_id upsert")
    exit_with_status()


if __name__ == "__main__":
    main()
