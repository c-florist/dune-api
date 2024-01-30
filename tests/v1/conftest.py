import pytest


@pytest.fixture
def character_db_response():
    yield [
        {
            "titles": '["Duke"]',
            "aliases": '["The Red Duke", "Leto the Just"]',
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
            "aliases": None,
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
            "aliases": None,
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


@pytest.fixture
def house_db_response():
    yield [
        {
            "name": "House Atreides",
            "homeworld": '["Caladan", "Arrakis"]',
            "status": "House Major",
            "colours": '["Red", "Green"]',
            "symbol": "Red Hawk",
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "name": "House Harkonnen",
            "homeworld": '["Giedi Prime"]',
            "status": "House Major",
            "colours": '["Blue", "Orange"]',
            "symbol": "Griffin",
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
    ]


@pytest.fixture
def organisation_db_response():
    yield [
        {
            "name": "Bene Gesserit",
            "founded": "c. 98 BG",
            "dissolved": None,
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "name": "Fremen",
            "founded": "c. 1300 BG",
            "dissolved": "c. 10219 AG",
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
    ]
