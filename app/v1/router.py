from sqlite3 import Connection
from typing import Any, Annotated

from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import RedirectResponse

from .response_models import Character, House, Organisation
from .dependencies import get_db_connection, CommonQueryParams
from .queries import read_characters, read_houses, read_organisations

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
    characters = read_characters(
        db_conn, house, common_query_params["skip"], common_query_params["limit"]
    )

    if not characters and house is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, House {house.capitalize()} does not exist",
        )

    return characters


@router.get("/houses", response_model=list[House])
def get_houses(
    common_query_params: CommonQueryParams,
    status: Annotated[
        str | None, Query(strict=True, examples=["Major", "major"])
    ] = None,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    houses = read_houses(
        db_conn, status, common_query_params["skip"], common_query_params["limit"]
    )

    if not houses and status is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, status House {status.capitalize()} does not exist",
        )

    return houses


@router.get("/organisations", response_model=list[Organisation])
def get_organisations(
    common_query_params: CommonQueryParams,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    organisations = read_organisations(db_conn, common_query_params["skip"], common_query_params["limit"])

    if not organisations:
        raise HTTPException(
            status_code=404,
            detail="Items not found"
        )

    return organisations
