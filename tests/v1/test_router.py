import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def test_client():
    yield TestClient(app)


def test_root_redirect_response(test_client):
    response = test_client.get("/v1")
    assert response.url.path == "/docs"


def test_get_all_characters(test_client):
    response = test_client.get("/v1/characters")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 5


def test_get_characters_by_house_success(test_client):
    response = test_client.get("/v1/characters?house=harkonnen")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 1
    assert all(x["house"] == "House Harkonnen" for x in data)


def test_get_characters_by_non_existent_house(test_client):
    response = test_client.get("/v1/characters?house=monkey")
    assert response.status_code == 404
    assert response.json()["detail"] == "Items not found, House Monkey does not exist"


def test_get_all_houses(test_client):
    response = test_client.get("/v1/houses")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 2


def test_get_houses_by_status_success(test_client):
    response = test_client.get("/v1/houses?status=major")
    assert response.status_code == 200
    assert all(x["status"] == "House Major" for x in response.json()["items"])


def test_get_houses_by_non_existent_status(test_client):
    response = test_client.get("/v1/houses?status=nope")
    assert response.status_code == 404
    assert (
        response.json()["detail"] == "Items not found, status House Nope does not exist"
    )


def test_get_all_organisations(test_client):
    response = test_client.get("/v1/organisations")
    assert response.status_code == 200
    data = response.json()["items"]
    assert len(data) == 3
