from typing import Any


def merge_dict(left: dict[str, Any] | None, right: dict[str, Any] | None) -> dict[str, Any]:
    merged: dict[str, Any] = dict(left or {})
    if right:
        merged.update(right)
    return merged


def _merge_by_id_list(
    left: list[Any] | None,
    right: list[Any] | None,
    id_attr: str = "id",
) -> list[Any]:
    by_id: dict[str, Any] = {}
    for item in left or []:
        key = getattr(item, id_attr, None) if not isinstance(item, dict) else item.get(id_attr)
        if key is not None:
            by_id[str(key)] = item
    for item in right or []:
        key = getattr(item, id_attr, None) if not isinstance(item, dict) else item.get(id_attr)
        if key is not None:
            by_id[str(key)] = item
    return list(by_id.values())


def merge_by_id(left: list[Any] | None, right: list[Any] | None) -> list[Any]:
    return _merge_by_id_list(left, right, "id")
