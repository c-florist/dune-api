from collections.abc import Generator
from sqlite3 import Connection
from typing import Annotated

from fastapi import Depends, Query

from .database import DbClient
from app.constants import DB_PATH


def get_db_connection() -> Generator[Connection, None, None]:
    db_client = DbClient(DB_PATH)
    try:
        yield db_client.conn
    finally:
        db_client.close()


def common_query_parameters(
    limit: int = Query(20, ge=0), offset: int = Query(0, ge=0)
) -> dict[str, int]:
    return {"limit": limit, "offset": offset}


CommonQueryParams = Annotated[dict[str, int], Depends(common_query_parameters)]
