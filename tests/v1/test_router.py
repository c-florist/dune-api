import pytest
from fastapi.testclient import TestClient

from app.main import app
from tests.setup.teardown import teardown_annotations


@pytest.fixture(autouse=True)
def run_around_tests(db_client):
    yield
    teardown_annotations(db_client.conn)


@pytest.fixture
def test_client():
    yield TestClient(app)


def test_root_redirect_response(test_client):
    response = test_client.get("/v1")
    assert response.url.path == "/docs"


def test_get_character_by_uuid(test_client):
    response = test_client.get("/v1/character/540b8c10-8297-4710-833e-84ef51797ac0")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Paul"
    assert data["last_name"] == "Atreides"


def test_get_all_characters(test_client):
    response = test_client.get("/v1/characters")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 5
    assert all(x.get("uuid") for x in data)


def test_get_characters_by_house_success(test_client):
    response = test_client.get("/v1/characters?house=harkonnen")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 1
    assert all(x["house"] == "House Harkonnen" for x in data)
    assert all(x.get("uuid") for x in data)


def test_get_characters_by_non_existent_house(test_client):
    response = test_client.get("/v1/characters?house=monkey")
    assert response.status_code == 404
    assert response.json()["detail"] == "Items not found, House Monkey does not exist"


def test_get_all_houses(test_client):
    response = test_client.get("/v1/houses")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 2
    assert all(x.get("uuid") for x in data)


def test_get_houses_by_status_success(test_client):
    response = test_client.get("/v1/houses?status=major")
    assert response.status_code == 200
    assert all(x["status"] == "House Major" for x in response.json()["items"])


def test_get_houses_by_non_existent_status(test_client):
    response = test_client.get("/v1/houses?status=nope")
    assert response.status_code == 404
    assert response.json()["detail"] == "Items not found, status House Nope does not exist"


def test_get_all_organisations(test_client):
    response = test_client.get("/v1/organisations")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 3
    assert all(x.get("uuid") for x in data)


def test_get_planet_by_uuid(test_client):
    response = test_client.get("/v1/planet/a370cbcd-d6e8-46bd-8a9f-bfd2fe5a8eef")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Arrakis"


def test_get_all_planets(test_client):
    response = test_client.get("/v1/planets")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 3
    assert all(x.get("uuid") for x in data)


def test_search_characters_success(test_client):
    response = test_client.get("/v1/characters/search?q=paul")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 1
    assert data[0]["first_name"] == "Paul"


def test_search_characters_not_found(test_client):
    response = test_client.get("/v1/characters/search?q=zaphod")
    assert response.status_code == 404
    assert response.json()["detail"] == "No characters found matching 'zaphod'"


def test_search_houses_success(test_client):
    response = test_client.get("/v1/houses/search?q=harkonnen")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 1
    assert data[0]["name"] == "House Harkonnen"


def test_search_houses_not_found(test_client):
    response = test_client.get("/v1/houses/search?q=beeblebrox")
    assert response.status_code == 404
    assert response.json()["detail"] == "No houses found matching 'beeblebrox'"


def test_get_planet_by_coords_success(test_client, monkeypatch):
    async def mock_get_environment_from_coords(self, lat, lon):
        return "desert"

    from app.services import geospatial_service

    monkeypatch.setattr(
        geospatial_service.GeoSpatialService,
        "get_environment_from_coords",
        mock_get_environment_from_coords,
    )

    response = test_client.post("/v1/planet/locate", json={"latitude": 32.7, "longitude": -114.8})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Arrakis"


def test_get_planet_by_coords_not_found(test_client, monkeypatch):
    async def mock_get_environment_from_coords(self, lat, lon):
        return "jungle"

    from app.services import geospatial_service

    monkeypatch.setattr(
        geospatial_service.GeoSpatialService,
        "get_environment_from_coords",
        mock_get_environment_from_coords,
    )

    response = test_client.post("/v1/planet/locate", json={"latitude": -1.9, "longitude": -55.9})
    assert response.status_code == 404
    assert response.json()["detail"] == "No planet found with environment similar to 'jungle'"


def test_create_annotation_for_character(test_client):
    response = test_client.post(
        "/v1/character/540b8c10-8297-4710-833e-84ef51797ac0/annotation",
        json={
            "user_id": "test_user",
            "annotation_text": "This is a test annotation.",
            "is_public": True,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == "test_user"
    assert data["annotation_text"] == "This is a test annotation."
    assert data["is_public"] is True


def test_get_user_annotations(test_client):
    response = test_client.post(
        "/v1/character/540b8c10-8297-4710-833e-84ef51797ac0/annotation",
        json={
            "user_id": "test_user",
            "annotation_text": "This is a test annotation.",
            "is_public": True,
        },
    )
    assert response.status_code == 201

    response = test_client.get("/v1/users/test_user/annotations")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 1
    assert data[0]["user_id"] == "test_user"


def test_update_annotation_success(test_client):
    response = test_client.post(
        "/v1/character/540b8c10-8297-4710-833e-84ef51797ac0/annotation",
        json={
            "user_id": "test_user",
            "annotation_text": "This is a test annotation.",
            "is_public": True,
        },
    )
    assert response.status_code == 201
    annotation_uuid = response.json()["uuid"]

    response = test_client.put(
        f"/v1/annotations/{annotation_uuid}",
        params={"user_id": "test_user"},
        json={"text": "This is an updated annotation.", "is_public": False},
    )
    assert response.status_code == 200
    assert response.json() == {"success": True}


def test_update_annotation_not_found(test_client):
    response = test_client.put(
        "/v1/annotations/some-uuid",
        params={"user_id": "test_user"},
        json={"text": "This is an updated annotation.", "is_public": False},
    )
    assert response.status_code == 404


def test_delete_annotation_success(test_client):
    response = test_client.post(
        "/v1/character/540b8c10-8297-4710-833e-84ef51797ac0/annotation",
        json={
            "user_id": "test_user",
            "annotation_text": "This is a test annotation.",
            "is_public": True,
        },
    )
    assert response.status_code == 201
    annotation_uuid = response.json()["uuid"]

    response = test_client.delete(f"/v1/annotations/{annotation_uuid}", params={"user_id": "test_user"})
    assert response.status_code == 200
    assert response.json() == {"success": True}


def test_delete_annotation_not_found(test_client):
    response = test_client.delete("/v1/annotations/some-uuid", params={"user_id": "test_user"})
    assert response.status_code == 404
