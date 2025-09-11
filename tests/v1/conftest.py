import pytest


@pytest.fixture
def character_db_response():
    # This response should reflect the data returned by the `character_with_org` view
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
            "profession": '["Ruler", "Soldier"]',
            "misc": None,
            "house": "House Atreides",
            "organisations": "[]",
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
            "dod": "Unknown",
            "profession": '["Soldier"]',
            "misc": None,
            "house": "House Atreides",
            "organisations": "[]",
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
            "profession": '["Ruler"]',
            "misc": None,
            "house": "House Harkonnen",
            "organisations": "[]",
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "titles": '["Duke", "Padishah Emperor", "Kwisatz Haderach", "Mahdi", "Lisan al Gaib"]',
            "aliases": '["MuadDib", "Usul", "The Preacher", "The Mentat Emperor"]',
            "first_name": "Paul",
            "last_name": "Atreides",
            "suffix": None,
            "dob": "10176 AG",
            "birthplace": "Caladan",
            "dod": "10219 AG",
            "profession": '["Ruler", "Soldier"]',
            "misc": None,
            "house": "House Atreides",
            "organisations": '["Fremen"]',
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "titles": '["Captain"]',
            "aliases": '["The Leaper"]',
            "first_name": "Chatt",
            "last_name": None,
            "suffix": None,
            "dob": "Unknown",
            "birthplace": "Unknown",
            "dod": "Unknown",
            "profession": '["Fighter"]',
            "misc": "Leader of the Fedaykin.",
            "house": None,
            "organisations": '["Fremen", "Fedaykin"]',
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
            "dissolved": "Unknown",
            "misc": None,
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "name": "Fremen",
            "founded": "c. 1300 BG",
            "dissolved": "c. 10219 AG",
            "misc": None,
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
        {
            "name": "Fedaykin",
            "founded": "Unknown",
            "dissolved": "10210 AG",
            "misc": "Originally a word used to describe the Fremen's guerilla fighters, later used in reference to Muad'Dib's personal guard, otherwise known as his death commandos.",
            "created_at": "2024-01-16 06:15:49",
            "updated_at": "2024-01-16 06:15:49",
        },
    ]