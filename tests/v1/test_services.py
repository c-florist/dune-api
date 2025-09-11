import httpx
import pytest

from app.v1.services import (
    EnvironmentService,
    InvalidResponseError,
    ServiceCommunicationError,
)


class MockSuccessResponse:
    """A mock response for a successful API call."""
    status_code = 200

    def json(self):
        return {"biomes": {"label": "Deserts & Xeric Shrublands"}}

    def raise_for_status(self):
        pass


class MockUnmappableResponse:
    """A mock response for a biome that isn't in our BIOME_MAP."""
    status_code = 200

    def json(self):
        return {"biomes": {"label": "Unmappable Biome"}}

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
    async def mock_get(*args, **kwargs):
        return MockSuccessResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        environment = await service.get_environment_from_coords(lat=27.98, lon=86.92)

    assert environment == "Desert"


@pytest.mark.asyncio
async def test_get_environment_from_coords_api_error(monkeypatch):
    async def mock_get(*args, **kwargs):
        return MockErrorResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        with pytest.raises(ServiceCommunicationError):
            await service.get_environment_from_coords(lat=27.98, lon=86.92)


@pytest.mark.asyncio
async def test_get_environment_from_coords_bad_json(monkeypatch):
    async def mock_get(*args, **kwargs):
        return MockBadJSONResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        with pytest.raises(InvalidResponseError):
            await service.get_environment_from_coords(lat=27.98, lon=86.92)


@pytest.mark.asyncio
async def test_get_environment_from_coords_unmappable_biome(monkeypatch):
    async def mock_get(*args, **kwargs):
        return MockUnmappableResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    async with httpx.AsyncClient() as client:
        service = EnvironmentService(client)
        with pytest.raises(InvalidResponseError):
            await service.get_environment_from_coords(lat=27.98, lon=86.92)
