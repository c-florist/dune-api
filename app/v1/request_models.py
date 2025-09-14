from pydantic import BaseModel


class AnnotationCreate(BaseModel):
    user_id: str
    text: str
    is_public: bool = False


class AnnotationUpdate(BaseModel):
    text: str | None = None
    is_public: bool | None = None


class Coordinates(BaseModel):
    latitude: float
    longitude: float
