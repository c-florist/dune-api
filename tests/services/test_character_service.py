
from sqlite3 import Connection

import app.v1.queries as queries
from app.domain.models import Character
from app.services.character_service import CharacterService


def test_get_character_by_uuid_returns_domain_model(monkeypatch):
    character_uuid = "some-uuid"
    character_data = {
        "uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "titles": '["Duke"]',
        "aliases": '["The Preacher"]',
        "first_name": "Paul",
        "last_name": "Atreides",
        "suffix": None,
        "dob": "10175 AG",
        "birthplace": "Kaitain",
        "dod": "10219 AG",
        "profession": '["Mentat", "Emperor"]',
        "misc": None,
        "house": "House Atreides",
        "organisations": '["Bene Gesserit", "Fremen"]',
    }

    def mock_read_character(db_conn: Connection, uuid: str):
        return character_data

    monkeypatch.setattr(queries, "read_character", mock_read_character)

    service = CharacterService(db_conn=None)
    result = service.get_character_by_uuid(character_uuid)

    assert isinstance(result, Character)
    assert result.first_name == "Paul"
    assert result.titles == ["Duke"]
