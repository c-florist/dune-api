from collections.abc import Generator
from sqlite3 import Connection
from typing import Annotated

from fastapi import Depends

from .database import DbClient
from .constants import DB_PATH


def get_db_connection() -> Generator[Connection, None, None]:
    db_client = DbClient(DB_PATH)
    try:
        yield db_client.conn
    finally:
        db_client.close()


def common_query_parameters(skip: int = 0, limit: int = 20) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


CommonQueryParams = Annotated[dict[str, int], Depends(common_query_parameters)]
