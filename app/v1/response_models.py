from pydantic import BaseModel

from app.domain.models import Character, House, Organisation, Planet


class PaginatedResponse(BaseModel):
    items: list[Character | House | Organisation | Planet]
    limit: int
    offset: int
    total: int


class SuccessResponse(BaseModel):
    success: bool
