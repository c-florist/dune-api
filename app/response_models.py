from pydantic import BaseModel, ConfigDict


class CustomBase(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Root(BaseModel):
    v1: dict[str, str]
