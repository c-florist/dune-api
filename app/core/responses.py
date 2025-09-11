from app.core.types import PydanticBoundModel


def paginated_response(
    items: list[PydanticBoundModel], limit: int, offset: int
) -> dict[str, int | list[PydanticBoundModel]]:
    return {"items": items, "limit": limit, "offset": offset, "total": len(items)}
