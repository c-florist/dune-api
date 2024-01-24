import pytest
import json
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def test_client():
    yield TestClient(app)


def test_root_redirect_response(test_client):
    response = test_client.get("/v1")
    assert response.url.path == "/docs"


def test_get_all_characters(test_client, character_db_response):
    response = test_client.get("/v1/characters")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 3

    assert [x["titles"] for x in data] == [
        json.loads(x["titles"]) for x in character_db_response
    ]


def test_get_characters_by_house_success(test_client):
    response = test_client.get("/v1/characters?house=harkonnen")
    assert response.status_code == 200
    assert all(x["house"] == "House Harkonnen" for x in response.json())


def test_get_characters_by_non_existent_house(test_client):
    response = test_client.get("/v1/characters?house=monkey")
    assert response.status_code == 404
    assert response.json() == {"detail": "Items not found, House Monkey does not exist"}
