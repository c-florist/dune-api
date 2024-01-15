from sqlite3 import Connection

from .response_models import Character


def get_characters(conn: Connection) -> list[Character]:
    ...
