import httpx
from pydantic import BaseModel, ValidationError


class ServiceCommunicationError(Exception):
    """Raised when there's a network or API error communicating with an external service."""

    pass


class InvalidResponseError(Exception):
    """Raised when the external service response is not in the expected format."""

    pass


BIOME_MAP = {
    "Deserts & Xeric Shrublands": "Desert",
    "Tropical & Subtropical Moist Broadleaf Forests": "Forest",
    "Temperate Conifer Forests": "Forest",
    "Boreal Forests/Taiga": "Forest",
    "Flooded Grasslands & Savannas": "Grassland",
    "Mangroves": "Coastal",
    "Inland Water": "Ocean",
    "Marine": "Ocean",
}


class Biome(BaseModel):
    """Represents the 'biomes' part of the OpenLandMap response."""

    label: str


class LandMapResponse(BaseModel):
    """Represents the top-level structure of the OpenLandMap response."""

    biomes: Biome


class EnvironmentService:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get_environment_from_coords(self, lat: float, lon: float) -> str:
        """
        Fetches biome data from OpenLandMap and maps it to a Dune environment.

        Raises:
            ServiceCommunicationError: If the external API call fails.
            InvalidResponseError: If the API response is malformed or unmappable.
        """
        try:
            url = f"https://api.openlandmap.org/query/point?lat={lat}&lon={lon}&layers=biomes"
            response = await self.client.get(url)
            response.raise_for_status()
            data = response.json()

            response_data = LandMapResponse(**data)
            biome_name = response_data.biomes.label

            environment = BIOME_MAP.get(biome_name)
            if environment is None:
                raise InvalidResponseError(f"Biome '{biome_name}' has no defined mapping.")

            return environment

        except httpx.HTTPStatusError as e:
            raise ServiceCommunicationError(f"External API returned a non-2xx status: {e.response.status_code}") from e
        except ValidationError as e:
            raise InvalidResponseError("External API response did not match expected format.") from e
        except (KeyError, TypeError) as e:
            raise InvalidResponseError("Could not parse the external API response.") from e
