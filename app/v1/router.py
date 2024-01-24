from sqlite3 import Connection
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from .response_models import Character
from .dependencies import get_db_connection, CommonQueryParams
from .queries import read_characters, read_characters_by_house

router = APIRouter()


@router.get("/", response_class=RedirectResponse)
async def root() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/characters", response_model=list[Character])
def get_all_characters(
    common_group_params: CommonQueryParams,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    characters = read_characters(db_conn, common_group_params["skip"], common_group_params["limit"])
    return characters


@router.get("/characters/{house}", response_model=list[Character])
def get_characters_by_house(
    common_group_params: CommonQueryParams,
    house: str,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    characters = read_characters_by_house(db_conn, house, common_group_params["skip"], common_group_params["limit"])
    return characters
