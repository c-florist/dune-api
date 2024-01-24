from sqlite3 import Connection
from typing import Any, Annotated

from fastapi import APIRouter, Depends, Query
from fastapi.responses import RedirectResponse

from .response_models import Character
from .dependencies import get_db_connection, CommonQueryParams
from .queries import read_characters, read_characters_by_house

router = APIRouter()


@router.get("/", response_class=RedirectResponse)
async def root() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/characters", response_model=list[Character])
def get_characters(
    common_query_params: CommonQueryParams,
    house: Annotated[
        str | None, Query(strict=True, examples=["Atreides", "atreides"])
    ] = None,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    if house is not None:
        characters = read_characters_by_house(
            db_conn, house, common_query_params["skip"], common_query_params["limit"]
        )
    else:
        characters = read_characters(
            db_conn, common_query_params["skip"], common_query_params["limit"]
        )

    return characters
