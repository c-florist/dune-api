from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import House
from app.services.house_service import HouseService


def test_get_houses_returns_domain_model(monkeypatch):
    house_data = [
        {
            "uuid": "e6cef093-fad8-4448-8bbf-86bad9fc8d85",
            "name": "House Atreides",
            "homeworld": '["Caladan", "Arrakis"]',
            "status": "House Major",
            "colours": '["Red", "Green"]',
            "symbol": "Red Hawk",
        }
    ]

    def mock_read_houses(db_conn: Connection, status: str | None, limit: int, offset: int):
        return house_data

    monkeypatch.setattr(queries, "read_houses", mock_read_houses)

    service = HouseService(db_conn=None)
    result = service.get_houses(status=None, limit=20, offset=0)

    assert isinstance(result[0], House)
    assert result[0].name == "House Atreides"
    assert result[0].homeworld == ["Caladan", "Arrakis"]
