from datetime import datetime

from pydantic import BaseModel


class Character(BaseModel):
    titles: list[str] | None
    first_name: str
    last_name: str
    relation: str | None
    organisation: str | None
    created_at: datetime
    updated_at: datetime


class Organisation(BaseModel):
    name: str
    year_founded: str | None
    created_at: datetime
    updated_at: datetime
