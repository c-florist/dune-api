from app.v1.queries import (
    read_character,
    read_characters,
    read_random_character,
    read_houses,
    read_organisations,
)


def test_read_character(db_client):
    character = read_character(db_client.conn, "540b8c10-8297-4710-833e-84ef51797ac0")
    assert character["first_name"] == "Paul"
    assert character["last_name"] == "Atreides"


def test_read_characters(db_client):
    characters = read_characters(db_client.conn)
    assert len(characters) == 5
    for char in characters:
        assert isinstance(char["first_name"], str)
        assert isinstance(char["last_name"], (str, type(None)))


def test_read_characters_by_house(db_client):
    characters = read_characters(db_client.conn, "atreides")
    assert len(characters) == 3
    assert all(c["house"] == "House Atreides" for c in characters)


def test_read_random_character(db_client):
    character = read_random_character(db_client.conn)
    assert character["first_name"] is not None


def test_read_houses(db_client):
    houses = read_houses(db_client.conn)
    assert len(houses) == 2


def test_read_houses_by_status(db_client):
    houses = read_houses(db_client.conn, "major")
    assert len(houses) == 2
    assert all(h["status"] == "House Major" for h in houses)


def test_read_organisations(db_client):
    orgs = read_organisations(db_client.conn)
    assert len(orgs) == 3
