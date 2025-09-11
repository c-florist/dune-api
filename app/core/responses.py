from typing import Any


def paginated_response(items: list[dict[str, Any]], limit: int, offset: int) -> dict[str, int | list[dict[str, Any]]]:
    return {"items": items, "limit": limit, "offset": offset, "total": len(items)}
