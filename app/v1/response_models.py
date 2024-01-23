from datetime import datetime
from typing import TypedDict

from pydantic import BaseModel, ConfigDict, Json


class CustomBase(BaseModel):
    model_config: TypedDict = ConfigDict(extra="forbid")

    created_at: datetime
    updated_at: datetime


class Character(CustomBase):
    titles: Json[list[str]] | None
    first_name: str
    last_name: str
    suffix: str | None
    dob: str
    birthplace: str
    dod: str | None
    house: str | None
    organisation: str | None
