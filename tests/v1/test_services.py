import httpx
import pytest

from app.v1.services import EnvironmentService


class MockSuccessResponse:
    """A mock response for a successful API call."""
    status_code = 200

    def json(self):
        return {"biomes": {"label": "Deserts & Xeric Shrublands"}}

    def raise_for_status(self):
        pass


class MockErrorResponse:
    """A mock response for a failed API call (e.g., 500 error)."""
    status_code = 500

    def json(self):
        return {"error": "Internal Server Error"}

    def raise_for_status(self):
        raise httpx.HTTPStatusError(
            message="Server Error", request=None, response=self
        )


class MockBadJSONResponse:
    """A mock response with an unexpected JSON structure."""
    status_code = 200

    def json(self):
        return {"some_other_key": "some_value"}

    def raise_for_status(self):
        pass


@pytest.mark.asyncio
async def test_get_environment_from_coords_success(monkeypatch):
    """
    Tests the success case where the external API returns a valid biome.
    """
    async def mock_get(*args, **kwargs):
        return MockSuccessResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        environment = await service.get_environment_from_coords(lat=27.98, lon=86.92)

    assert environment == "Desert"


@pytest.mark.asyncio
async def test_get_environment_from_coords_api_error(monkeypatch):
    """
    Tests the failure case where the external API returns a non-2xx status code.
    """
    async def mock_get(*args, **kwargs):
        return MockErrorResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        environment = await service.get_environment_from_coords(lat=27.98, lon=86.92)

    assert environment is None


@pytest.mark.asyncio
async def test_get_environment_from_coords_bad_json(monkeypatch):
    """
    Tests the failure case where the external API returns an unexpected JSON structure.
    """
    async def mock_get(*args, **kwargs):
        return MockBadJSONResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        environment = await service.get_environment_from_coords(lat=27.98, lon=86.92)

    assert environment is None
