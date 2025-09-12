from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import House


class HouseService:
    db_conn: Connection

    def __init__(self, db_conn: Connection) -> None:
        self.db_conn = db_conn

    def get_houses(self, status: str | None, limit: int, offset: int) -> list[House]:
        houses_data = queries.read_houses(self.db_conn, status, limit, offset)
        return [House(**house_data) for house_data in houses_data]

    def search_houses(self, search_term: str, limit: int, offset: int) -> list[House]:
        houses_data = queries.search_houses(self.db_conn, search_term, limit, offset)
        return [House(**house_data) for house_data in houses_data]
