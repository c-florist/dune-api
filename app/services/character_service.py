from sqlite3 import Connection
from typing import Any

import app.v1.queries as queries


class CharacterService:
    def __init__(self, db_conn: Connection):
        self.db_conn = db_conn

    def get_character_by_uuid(self, uuid: str) -> dict[str, Any] | None:
        return queries.read_character(self.db_conn, uuid)

    def get_characters(self, house: str | None, limit: int, offset: int) -> list[dict[str, Any]]:
        return queries.read_characters(self.db_conn, house, limit, offset)

    def get_random_character(self) -> dict[str, Any] | None:
        return queries.read_random_character(self.db_conn)
