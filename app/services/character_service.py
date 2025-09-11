from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Character


class CharacterService:
    db_conn: Connection

    def __init__(self, db_conn: Connection) -> None:
        self.db_conn = db_conn

    def get_character_by_uuid(self, uuid: str) -> Character | None:
        character_data = queries.read_character(self.db_conn, uuid)
        if character_data:
            return Character(**character_data)
        return None

    def get_characters(self, house: str | None, limit: int, offset: int) -> list[Character]:
        characters_data = queries.read_characters(self.db_conn, house, limit, offset)
        return [Character(**character_data) for character_data in characters_data]

    def get_random_character(self) -> Character | None:
        character_data = queries.read_random_character(self.db_conn)
        if character_data:
            return Character(**character_data)
        return None
