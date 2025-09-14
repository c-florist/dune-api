import uuid

import pytest
from app.v1.queries import (
    create_annotation,
    read_annotations_for_target,
    read_annotations_for_user,
    read_character,
    read_characters,
    read_houses,
    read_organisations,
    read_planet,
    read_planets,
    read_random_character,
    search_characters,
    search_houses,
    update_annotation,
    delete_annotation,
)
from tests.setup.teardown import teardown_annotations


@pytest.fixture(autouse=True)
def run_around_tests(db_client):
    yield
    teardown_annotations(db_client.conn)


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


def test_read_planet(db_client):
    planet = read_planet(db_client.conn, "a370cbcd-d6e8-46bd-8a9f-bfd2fe5a8eef")
    assert planet["name"] == "Arrakis"


def test_read_planets(db_client):
    planets = read_planets(db_client.conn)
    assert len(planets) == 3
    for planet in planets:
        assert isinstance(planet["name"], str)
        assert isinstance(planet["environment"], str)
        assert isinstance(planet["ruler"], (str, type(None)))


def test_search_characters(db_client):
    characters = search_characters(db_client.conn, "paul")
    assert len(characters) == 1
    assert characters[0]["first_name"] == "Paul"


def test_search_houses(db_client):
    houses = search_houses(db_client.conn, "harkonnen")
    assert len(houses) == 1
    assert houses[0]["name"] == "House Harkonnen"


def test_create_annotation(db_client):
    annotation_uuid = str(uuid.uuid4())
    annotation_data = {
        "uuid": annotation_uuid,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a test annotation.",
        "is_public": True,
    }
    annotation = create_annotation(db_client.conn, annotation_data)
    assert annotation["uuid"] == annotation_uuid
    assert annotation["user_id"] == "test_user"
    assert annotation["annotation_text"] == "This is a test annotation."
    assert annotation["is_public"] == 1


def test_read_annotations_for_target(db_client):
    annotation_uuid = str(uuid.uuid4())
    annotation_data = {
        "uuid": annotation_uuid,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a public annotation.",
        "is_public": True,
    }
    create_annotation(db_client.conn, annotation_data)

    annotation_uuid_private = str(uuid.uuid4())
    annotation_data_private = {
        "uuid": annotation_uuid_private,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a private annotation.",
        "is_public": False,
    }
    create_annotation(db_client.conn, annotation_data_private)

    annotations = read_annotations_for_target(db_client.conn, "character", "540b8c10-8297-4710-833e-84ef51797ac0")
    assert len(annotations) == 1
    assert annotations[0]["uuid"] == annotation_uuid
    assert annotations[0]["is_public"] == 1


def test_update_annotation_success(db_client):
    annotation_uuid = str(uuid.uuid4())
    annotation_data = {
        "uuid": annotation_uuid,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a test annotation.",
        "is_public": True,
    }
    create_annotation(db_client.conn, annotation_data)

    update_data = {
        "annotation_text": "This is an updated annotation.",
        "is_public": False,
    }
    result = update_annotation(db_client.conn, annotation_uuid, "test_user", update_data)
    assert result is True

    annotations = read_annotations_for_user(db_client.conn, "test_user")
    assert len(annotations) == 1
    updated_annotation = annotations[0]
    assert updated_annotation["annotation_text"] == "This is an updated annotation."
    assert updated_annotation["is_public"] == 0


def test_update_annotation_wrong_user(db_client):
    annotation_uuid = str(uuid.uuid4())
    annotation_data = {
        "uuid": annotation_uuid,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a test annotation.",
        "is_public": True,
    }
    create_annotation(db_client.conn, annotation_data)

    update_data = {
        "annotation_text": "This is an updated annotation.",
        "is_public": False,
    }
    result = update_annotation(db_client.conn, annotation_uuid, "wrong_user", update_data)
    assert result is False

    annotations = read_annotations_for_user(db_client.conn, "test_user")
    assert len(annotations) == 1
    updated_annotation = annotations[0]
    assert updated_annotation["annotation_text"] == "This is a test annotation."
    assert updated_annotation["is_public"] == 1


def test_delete_annotation_success(db_client):
    annotation_uuid = str(uuid.uuid4())
    annotation_data = {
        "uuid": annotation_uuid,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a test annotation.",
        "is_public": True,
    }
    create_annotation(db_client.conn, annotation_data)

    result = delete_annotation(db_client.conn, annotation_uuid, "test_user")
    assert result is True

    annotations = read_annotations_for_user(db_client.conn, "test_user")
    assert len(annotations) == 0


def test_delete_annotation_wrong_user(db_client):
    annotation_uuid = str(uuid.uuid4())
    annotation_data = {
        "uuid": annotation_uuid,
        "user_id": "test_user",
        "target_type": "character",
        "target_uuid": "540b8c10-8297-4710-833e-84ef51797ac0",
        "annotation_text": "This is a test annotation.",
        "is_public": True,
    }
    create_annotation(db_client.conn, annotation_data)

    result = delete_annotation(db_client.conn, annotation_uuid, "wrong_user")
    assert result is False

    annotations = read_annotations_for_user(db_client.conn, "test_user")
    assert len(annotations) == 1
