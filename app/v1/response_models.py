from pydantic import BaseModel

from app.domain.models import Annotation, Character, House, Organisation, Planet


class PaginatedResponse(BaseModel):
    items: list[Character | House | Organisation | Planet | Annotation]
    limit: int
    offset: int
    total: int


class BoolResponse(BaseModel):
    success: bool
