from pydantic import BaseModel, Json

from ..response_models import CustomBase


class Character(CustomBase):
    titles: Json[list[str]] | None
    aliases: Json[list[str]] | None
    first_name: str
    last_name: str | None
    suffix: str | None
    dob: str
    birthplace: str
    dod: str | None
    profession: Json[list[str]] | None
    misc: str | None
    house: str | None
    organisations: Json[list[str]] | None


class House(CustomBase):
    name: str
    homeworld: Json[list[str]]
    status: str
    colours: Json[list[str]]
    symbol: str


class Organisation(CustomBase):
    name: str
    founded: str
    dissolved: str
    misc: str | None


class PaginatedResponse(BaseModel):
    items: list[Character | House | Organisation]
    limit: int
    offset: int
    total: int
