from pydantic import BaseModel


class Root(BaseModel):
    v1: dict[str, str]
