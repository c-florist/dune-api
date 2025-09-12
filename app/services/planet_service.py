from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Planet


class PlanetService:
    db_conn: Connection

    def __init__(self, db_conn: Connection) -> None:
        self.db_conn = db_conn

    def get_planets(self, limit: int, offset: int) -> list[Planet]:
        planets_data = queries.read_planets(self.db_conn, limit, offset)
        return [Planet(**planet_data) for planet_data in planets_data]

    def get_planet_by_uuid(self, uuid: str) -> Planet | None:
        planet_data = queries.read_planet(self.db_conn, uuid)
        if planet_data:
            return Planet(**planet_data)
        return None
