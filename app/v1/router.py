from sqlite3 import Connection
from typing import Any, Annotated

from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import RedirectResponse

from .response_models import Character
from .dependencies import get_db_connection, CommonQueryParams
from .queries import read_characters

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
    characters = read_characters(db_conn, house, common_query_params["skip"], common_query_params["limit"])

    if not characters and house is not None:
        raise HTTPException(status_code=404, detail=f"Items not found, House {house.capitalize()} does not exist")

    return characters
