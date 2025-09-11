from pydantic import UUID4, BaseModel, Json

from ..response_models import CustomBase


class Character(CustomBase):
    uuid: UUID4
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
    uuid: UUID4
    name: str
    homeworld: Json[list[str]]
    status: str
    colours: Json[list[str]]
    symbol: str


class Organisation(CustomBase):
    uuid: UUID4
    name: str
    founded: str
    dissolved: str
    misc: str | None


class Planet(CustomBase):
    uuid: UUID4
    name: str
    environment: str
    ruler: str | None


class PaginatedResponse(BaseModel):
    items: list[Character | House | Organisation | Planet]
    limit: int
    offset: int
    total: int
