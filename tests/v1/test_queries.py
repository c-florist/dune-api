import json
import pytest
from contextlib import closing

from app.v1.queries import get_characters, get_characters_by_house


@pytest.fixture
def house_raw_data():
    return [
        (
            1,
            "House Atreides",
            "Caladan",
            "House Major",
            json.dumps(["Red", "Green"]),
            "Red Hawk",
            "2024-01-16 06:15:49",
            "2024-01-16 06:15:49",
        ),
        (
            2,
            "House Harkonnen",
            "Giedi Prime",
            "House Major",
            json.dumps(["Blue", "Orange"]),
            "Ram",
            "2024-01-16 06:15:49",
            "2024-01-16 06:15:49",
        ),
    ]


@pytest.fixture
def character_raw_data():
    return [
        (
            json.dumps(["Duke"]),
            "Leto",
            "Atreides",
            "I",
            "10140 AG",
            "Caladan",
            "10191 AG",
            1,
            "2024-01-16 06:15:49",
            "2024-01-16 06:15:49",
        ),
        (
            json.dumps(["Warmaster", "Earl of Caladan"]),
            "Gurney",
            "Halleck",
            None,
            "10130s AG",
            "Unknown",
            None,
            1,
            "2024-01-16 06:15:49",
            "2024-01-16 06:15:49",
        ),
        (
            json.dumps(["Baron"]),
            "Vladimir",
            "Harkonnen",
            None,
            "10110 AG",
            "Giedi Prime",
            "10193 AG",
            2,
            "2024-01-16 06:15:49",
            "2024-01-16 06:15:49",
        ),
    ]


@pytest.fixture
def db_client(db_client, house_raw_data, character_raw_data):
    with closing(db_client.conn.cursor()) as cursor:
        cursor.executemany(
            "INSERT INTO house (id, name, homeworld, status, colours, symbol, created_at, updated_at) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            house_raw_data,
        )

        cursor.executemany(
            "INSERT INTO character (titles, first_name, last_name, suffix, dob, birthplace, dod, house_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            character_raw_data,
        )

    yield db_client


def test_get_characters(db_client, character_db_response):
    characters = get_characters(db_client.conn)

    assert characters == character_db_response


def test_get_characters_by_house(db_client, character_db_response):
    expected_response = [
        x for x in character_db_response if x["house"] == "House Atreides"
    ]
    characters = get_characters_by_house(db_client.conn, "House Atreides")

    assert characters == expected_response
