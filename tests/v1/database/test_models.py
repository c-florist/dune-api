import pytest

from app.v1.database.models import DbCharacter


@pytest.fixture
def db_response():
    yield {
        "titles": '["Duke"]',
        "first_name": "Leto",
        "last_name": "Atreides",
        "suffix": "I",
        "dob": "10140 AG",
        "birthplace": "Caladan",
        "dod": "10191 AG",
        "house": "House Atreides",
        "organisation": None,
        "created_at": "2024-01-16 06:15:49",
        "updated_at": "2024-01-16 06:15:49",
    }


def test_db_model_to_dict_converts_stringified_json(db_response):
    model = DbCharacter(**db_response)

    assert isinstance(model.titles, str)
    assert isinstance(model.to_dict(json_fields=("titles",))["titles"], list)
