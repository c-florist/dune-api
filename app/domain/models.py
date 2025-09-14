from pydantic import UUID4, BaseModel, ConfigDict, Json


class CustomBase(BaseModel):
    model_config = ConfigDict(extra="forbid")


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
    homeworld: Json[list[str]] | None
    status: str
    colours: Json[list[str]] | None
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


class Annotation(CustomBase):
    uuid: UUID4
    user_id: str
    target_type: str
    target_uuid: str
    text: str
    is_public: bool
