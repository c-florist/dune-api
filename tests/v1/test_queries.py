import json
import pytest
from contextlib import closing

from app.v1.queries import get_characters


def character_raw_data(house_id):
    return [
        (
            json.dumps(["Duke"]),
            "Leto",
            "Atreides",
            "I",
            "10140 AG",
            "Caladan",
            "10191 AG",
            house_id,
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
            house_id,
            "2024-01-16 06:15:49",
            "2024-01-16 06:15:49",
        ),
    ]


@pytest.fixture
def db_client(db_client):
    with closing(db_client.conn.cursor()) as cursor:
        cursor.execute(
            "INSERT INTO house (name, homeworld, status, colours, symbol, created_at, updated_at) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (
                "House Atreides",
                "Caladan",
                "House Major",
                json.dumps(["Red", "Green"]),
                "Red Hawk",
                "2024-01-16 06:15:49",
                "2024-01-16 06:15:49",
            ),
        )

        cursor.executemany(
            "INSERT INTO character (titles, first_name, last_name, suffix, dob, birthplace, dod, house_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            character_raw_data(cursor.lastrowid),
        )

    yield db_client


def test_get_characters(db_client, character_db_response):
    characters = get_characters(db_client.conn)

    assert characters == character_db_response
