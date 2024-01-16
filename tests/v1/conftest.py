import json
from contextlib import closing

import pytest


def generate_atreides_characters(house_id):
    return [
        (json.dumps(["Duke"]), "Leto", "Atreides", "I", "10140 AG", "Caladan", "10191 AG", house_id, "2024-01-16 06:15:49", "2024-01-16 06:15:49"),
        (json.dumps(["Warmaster", "Earl of Caladan"]), "Gurney", "Halleck", None, "10130s AG", "Unknown", None, house_id, "2024-01-16 06:15:49", "2024-01-16 06:15:49"),
    ]


@pytest.fixture
def db_client(db_client):
    with closing(db_client.conn.cursor()) as cursor:
        cursor.execute(
            "INSERT INTO house (name, homeworld, status, colours, symbol, created_at, updated_at) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ("House Atreides", "Caladan", "House Major", json.dumps(["Red", "Green"]), "Red Hawk", "2024-01-16 06:15:49", "2024-01-16 06:15:49")
        )

        cursor.executemany(
            "INSERT INTO character (titles, first_name, last_name, suffix, dob, birthplace, dod, house_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            generate_atreides_characters(cursor.lastrowid)
        )

    yield db_client

    with closing(db_client.conn.cursor()) as cursor:
        cursor.executescript("""
            DELETE FROM house;
            DELETE FROM character;
        """)
