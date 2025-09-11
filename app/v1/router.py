from logging import getLogger
from sqlite3 import Connection
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse
from pydantic import UUID4

from app.core.responses import paginated_response

from .dependencies import CommonQueryParams, get_db_connection, get_environment_service
from .queries import (
    read_character,
    read_characters,
    read_houses,
    read_organisations,
    read_planet,
    read_planet_by_environment,
    read_planets,
    read_random_character,
)
from .request_models import Coordinates
from .response_models import Character, PaginatedResponse, Planet
from .services import (
    EnvironmentService,
    InvalidResponseError,
    ServiceCommunicationError,
)

logger = getLogger(__name__)
router = APIRouter()


@router.get("/", response_class=RedirectResponse)
async def root() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/characters", response_model=PaginatedResponse)
def get_characters(
    common_query_params: CommonQueryParams,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
    house: Annotated[str | None, Query(strict=True, examples=["Atreides", "atreides"])] = None,
) -> Any:
    characters = read_characters(db_conn, house, common_query_params["limit"], common_query_params["offset"])

    if not characters and house is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, House {house.capitalize()} does not exist",
        )

    return paginated_response(characters, common_query_params["limit"], common_query_params["offset"])


@router.get("/character/{uuid}", response_model=Character)
def get_character(
    uuid: str,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
) -> Any:
    character = read_character(db_conn, uuid)

    if not character:
        raise HTTPException(status_code=404, detail=f"Character {uuid} not found")

    return character


@router.get("/character/random", response_model=PaginatedResponse)
def get_random_character(db_conn: Annotated[Connection, Depends(get_db_connection)]) -> Any:
    character = read_random_character(db_conn)

    if not character:
        logger.error("Could not get a random character from database")
        raise HTTPException(status_code=500, detail="No data available")

    return paginated_response([character], 0, 0)


@router.get("/houses", response_model=PaginatedResponse)
def get_houses(
    common_query_params: CommonQueryParams,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
    status: Annotated[str | None, Query(strict=True, examples=["Major", "major"])] = None,
) -> Any:
    houses = read_houses(db_conn, status, common_query_params["limit"], common_query_params["offset"])

    if not houses and status is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, status House {status.capitalize()} does not exist",
        )

    return paginated_response(houses, common_query_params["limit"], common_query_params["offset"])


@router.get("/organisations", response_model=PaginatedResponse)
def get_organisations(
    common_query_params: CommonQueryParams,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
) -> Any:
    organisations = read_organisations(db_conn, common_query_params["limit"], common_query_params["offset"])

    if not organisations:
        raise HTTPException(status_code=404, detail="Items not found")

    return paginated_response(organisations, common_query_params["limit"], common_query_params["offset"])


@router.post("/planet/from-coordinates", response_model=Planet)
async def get_planet_from_coordinates(
    coordinates: Coordinates,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
    environment_service: Annotated[EnvironmentService, Depends(get_environment_service)],
) -> Any:
    try:
        environment = await environment_service.get_environment_from_coords(coordinates.latitude, coordinates.longitude)
    except ServiceCommunicationError as e:
        logger.error(f"Service communication error: {e}")
        raise HTTPException(status_code=503, detail="External service is unavailable") from None
    except InvalidResponseError as e:
        logger.error(f"Invalid response from service: {e}")
        raise HTTPException(status_code=500, detail="Error parsing external service response") from None

    planet = read_planet_by_environment(db_conn, environment)
    if not planet:
        raise HTTPException(status_code=404, detail=f"No planet found with environment: {environment}")

    return planet


@router.get("/planet/{uuid}", response_model=Planet)
def get_planet(
    uuid: UUID4,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
) -> Any:
    planet = read_planet(db_conn, str(uuid))

    if not planet:
        raise HTTPException(status_code=404, detail=f"Planet {uuid} not found")

    return planet


@router.get("/planets", response_model=PaginatedResponse)
def get_planets(
    common_query_params: CommonQueryParams,
    db_conn: Annotated[Connection, Depends(get_db_connection)],
) -> Any:
    planets = read_planets(db_conn, common_query_params["limit"], common_query_params["offset"])

    if not planets:
        raise HTTPException(status_code=404, detail="Items not found")

    return paginated_response(planets, common_query_params["limit"], common_query_params["offset"])
