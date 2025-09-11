from collections.abc import Generator
from sqlite3 import Connection
from typing import Annotated

from fastapi import Depends, Query

from app.core.constants import DB_PATH
from app.core.database import DBClient
from app.services.character_service import CharacterService
from app.services.house_service import HouseService


def get_db_connection() -> Generator[Connection]:
    db_client = DBClient(DB_PATH)
    try:
        yield db_client.conn
    finally:
        db_client.close()


def get_character_service(
    db_conn: Annotated[Connection, Depends(get_db_connection)],
) -> CharacterService:
    return CharacterService(db_conn)


def get_house_service(
    db_conn: Annotated[Connection, Depends(get_db_connection)],
) -> HouseService:
    return HouseService(db_conn)


def common_query_parameters(limit: int = Query(20, ge=0), offset: int = Query(0, ge=0)) -> dict[str, int]:
    return {"limit": limit, "offset": offset}


CommonQueryParams = Annotated[dict[str, int], Depends(common_query_parameters)]
