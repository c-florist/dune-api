from typing import TypeVar

from pydantic import BaseModel

PydanticBoundModel = TypeVar("PydanticBoundModel", bound=BaseModel)
