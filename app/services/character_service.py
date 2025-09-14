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

    def get_characters(self, house: str | None, limit: int, offset: int) -> tuple[list[Character], int]:
        characters_data, total = queries.read_characters(self.db_conn, house, limit, offset)
        characters = [Character(**character_data) for character_data in characters_data]
        return characters, total

    def get_random_character(self) -> Character | None:
        character_data = queries.read_random_character(self.db_conn)
        if character_data:
            return Character(**character_data)
        return None

    def search_characters(self, search_term: str, limit: int, offset: int) -> tuple[list[Character], int]:
        characters_data, total = queries.search_characters(self.db_conn, search_term, limit, offset)
        characters = [Character(**character_data) for character_data in characters_data]
        return characters, total
