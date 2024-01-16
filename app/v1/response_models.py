from datetime import datetime

from pydantic import BaseModel


class Character(BaseModel):
    titles: list[str] | None
    first_name: str
    last_name: str
    suffix: str | None
    dob: str
    birthplace: str
    dod: str | None
    house: str | None
    organisation: str | None
    created_at: datetime
    updated_at: datetime
