from app.v1.queries import read_characters, read_characters_by_house


def test_read_characters(db_client, character_db_response):
    characters = read_characters(db_client.conn)

    assert characters == character_db_response


def test_read_characters_by_house(db_client, character_db_response):
    expected_response = [
        x for x in character_db_response if x["house"] == "House Atreides"
    ]
    characters = read_characters_by_house(db_client.conn, "Atreides")

    assert characters == expected_response
