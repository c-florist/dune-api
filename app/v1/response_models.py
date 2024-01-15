from datetime import datetime

from pydantic import BaseModel


class Character(BaseModel):
    title: str | None
    first_name: str
    last_name: str
    relation: str | None
    organisation: str | None
    created_at: datetime
    updated_at: datetime
