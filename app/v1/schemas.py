import json
from dataclasses import dataclass
from typing import Any


class BaseSchema:
    def to_dict(self, json_fields: tuple[str, ...]) -> dict[str, Any]:
        _dict = self.__dict__.copy()
        for field in json_fields:
            _dict[field] = json.loads(_dict[field])

        return _dict


@dataclass
class CharacterSchema(BaseSchema):
    titles: str
    first_name: str
    last_name: str
    suffix: str | None
    dob: str
    birthplace: str
    dod: str | None
    house: str | None
    organisation: str | None
    created_at: str
    updated_at: str
