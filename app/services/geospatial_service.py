from logging import getLogger

import httpx
from fastapi import HTTPException
from pydantic import BaseModel

logger = getLogger(__name__)


class CurrentWeather(BaseModel):
    time: str
    temperature: float


class OpenMeteoResponse(BaseModel):
    elevation: float
    current_weather: CurrentWeather


class GeoSpatialService:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    async def get_environment_from_coords(self, lat: float, lon: float) -> str:
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.BASE_URL, params=params)
                response.raise_for_status()

                data = OpenMeteoResponse(**response.json())
                return self._map_weather_to_environment(data)
            except httpx.HTTPStatusError as e:
                logger.error(f"Error getting environment from coords: {e}")
                raise HTTPException(status_code=500, detail="Error getting environment from coords") from e
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                raise HTTPException(status_code=500, detail="An unexpected error occurred") from e

    def _map_weather_to_environment(self, data: OpenMeteoResponse) -> str:
        try:
            temp = int(data.current_weather.temperature)

            if temp > 30:
                return "desert"
            if temp < -10:
                return "ice"
            else:
                return "ocean"

        except (KeyError, IndexError) as e:
            logger.error(f"Error mapping weather to environment: {e}")
            raise HTTPException(status_code=500, detail="Error mapping weather to environment") from e
