from app.v1.queries import read_characters, read_houses, read_organisations


def test_read_characters(db_client, character_db_response):
    characters = read_characters(db_client.conn)

    assert characters == character_db_response


def test_read_characters_by_house(db_client, character_db_response):
    expected_response = [
        x for x in character_db_response if x["house"] == "House Atreides"
    ]
    characters = read_characters(db_client.conn, "atreides")

    assert characters == expected_response


def test_read_houses(db_client, house_db_response):
    houses = read_houses(db_client.conn)

    assert houses == house_db_response


def test_read_houses_by_status(db_client, house_db_response):
    expected_response = [x for x in house_db_response if x["status"] == "House Major"]
    houses = read_houses(db_client.conn, "major")

    assert houses == expected_response


def test_read_organisations(db_client, organisation_db_response):
    orgs = read_organisations(db_client.conn)

    assert orgs == organisation_db_response
