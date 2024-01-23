from sqlite3 import Connection
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from .response_models import Character
from .dependencies import get_db_connection
from .queries import get_characters

router = APIRouter()


@router.get("/", response_class=RedirectResponse)
async def root() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/characters", response_model=list[Character])
def get_all_characters(
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    characters = get_characters(db_conn)
    return characters
