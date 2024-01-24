from collections.abc import Generator
from sqlite3 import Connection
from typing import Annotated

from fastapi import Depends

from app.v1.database import db_client


def get_db_connection() -> Generator[Connection, None, None]:
    try:
        with db_client.conn as conn:
            yield conn
    finally:
        db_client.conn.close()


def common_group_parameters(skip: int = 0, limit: int = 20) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


CommonGroupParams = Annotated[dict, Depends(common_group_parameters)]
