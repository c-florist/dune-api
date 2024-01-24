import pytest


@pytest.fixture
def character_db_response():
    return [
        {
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
        },
        {
            "titles": '["Warmaster", "Earl of Caladan"]',
            "first_name": "Gurney",
            "last_name": "Halleck",
            "suffix": None,
            "dob": "10130s AG",
            "birthplace": "Unknown",
            "dod": None,
            "house": "House Atreides",
            "organisation": None,
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "titles": '["Baron"]',
            "first_name": "Vladimir",
            "last_name": "Harkonnen",
            "suffix": None,
            "dob": "10110 AG",
            "birthplace": "Giedi Prime",
            "dod": "10193 AG",
            "house": "House Harkonnen",
            "organisation": None,
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
    ]
