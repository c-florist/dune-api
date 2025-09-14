from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Planet
from app.services.planet_service import PlanetService


def test_get_planets_returns_domain_model(monkeypatch):
    planet_data = [
        {
            "uuid": "a370cbcd-d6e8-46bd-8a9f-bfd2fe5a8eef",
            "name": "Arrakis",
            "environment": "Desert",
            "ruler": "House Atreides",
        }
    ]

    def mock_read_planets(db_conn: Connection, limit: int, offset: int):
        return planet_data, len(planet_data)

    monkeypatch.setattr(queries, "read_planets", mock_read_planets)

    service = PlanetService(db_conn=None)
    result, total = service.get_planets(limit=20, offset=0)

    assert isinstance(result[0], Planet)
    assert result[0].name == "Arrakis"
    assert total == 1


def test_get_planet_by_uuid_returns_domain_model(monkeypatch):
    planet_uuid = "a370cbcd-d6e8-46bd-8a9f-bfd2fe5a8eef"
    planet_data = {
        "uuid": "a370cbcd-d6e8-46bd-8a9f-bfd2fe5a8eef",
        "name": "Arrakis",
        "environment": "Desert",
        "ruler": "House Atreides",
    }

    def mock_read_planet(db_conn: Connection, uuid: str):
        return planet_data

    monkeypatch.setattr(queries, "read_planet", mock_read_planet)

    service = PlanetService(db_conn=None)
    result = service.get_planet_by_uuid(planet_uuid)

    assert isinstance(result, Planet)
    assert result.name == "Arrakis"
