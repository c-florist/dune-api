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


def test_get_characters_returns_domain_models(monkeypatch):
    characters_data = [
        {
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
        },
        {
            "uuid": "14aee0b2-2517-4d6d-a4fb-b09008d67141",
            "titles": '["Baron"]',
            "aliases": None,
            "first_name": "Vladimir",
            "last_name": "Harkonnen",
            "suffix": None,
            "dob": "10110 AG",
            "birthplace": "Giedi Prime",
            "dod": "10193 AG",
            "profession": '["Ruler"]',
            "misc": None,
            "house": "House Harkonnen",
            "organisations": "[]",
        },
    ]

    def mock_read_characters(db_conn: Connection, house: str | None, limit: int, offset: int):
        return characters_data, len(characters_data)

    monkeypatch.setattr(queries, "read_characters", mock_read_characters)

    service = CharacterService(db_conn=None)
    result, total = service.get_characters(house=None, limit=20, offset=0)

    assert len(result) == 2
    assert total == 2
    assert isinstance(result[0], Character)
    assert isinstance(result[1], Character)
    assert result[0].first_name == "Paul"
    assert result[1].last_name == "Harkonnen"
