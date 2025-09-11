from collections import defaultdict
from logging import getLogger

from httpx import AsyncClient, HTTPStatusError
from pydantic import BaseModel, ValidationError

logger = getLogger(__name__)

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
    client: AsyncClient

    def __init__(self, client: AsyncClient):
        self.client = client

    async def get_environment_from_coords(self, lat: float, lon: float) -> str | None:
        """
        Fetches biome data from OpenLandMap and maps it to a Dune environment.
        """
        data = defaultdict()
        status_code = None
        try:
            url = f"https://api.openlandmap.org/query/point?lat={lat}&lon={lon}&layers=biomes"
            response = await self.client.get(url)
            status_code = response.status_code
            _ = response.raise_for_status()
            data = response.json()

            response_data = LandMapResponse(**data)
            biome_name = response_data.biomes.label

            return BIOME_MAP.get(biome_name)

        except HTTPStatusError:
            logger.error(f"Failed to fetch biome data from OpenLandMap: {status_code}")
            return None

        except ValidationError:
            logger.error(f"Failed to parse biome data from OpenLandMap: {data}")
            return None

        except (KeyError, TypeError):
            logger.error(f"Failed to extract biome data from OpenLandMap: {data}")
            return None
