from logging import getLogger
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse
from pydantic import UUID4

from app.core.responses import paginated_response
from app.domain.models import Character, Planet
from app.services.character_service import CharacterService
from app.services.house_service import HouseService
from app.services.organisation_service import OrganisationService
from app.services.planet_service import PlanetService

from .dependencies import (
    CommonQueryParams,
    get_character_service,
    get_house_service,
    get_organisation_service,
    get_planet_service,
)
from .response_models import PaginatedResponse

logger = getLogger(__name__)
router = APIRouter()


@router.get("/", response_class=RedirectResponse)
async def root() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/characters", response_model=PaginatedResponse)
def get_characters(
    common_query_params: CommonQueryParams,
    character_service: Annotated[CharacterService, Depends(get_character_service)],
    house: Annotated[str | None, Query(strict=True, examples=["Atreides", "atreides"])] = None,
) -> Any:
    characters = character_service.get_characters(house, common_query_params["limit"], common_query_params["offset"])

    if not characters and house is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, House {house.capitalize()} does not exist",
        )

    return paginated_response(characters, common_query_params["limit"], common_query_params["offset"])


@router.get("/character/{uuid}", response_model=Character)
def get_character(
    uuid: str,
    character_service: Annotated[CharacterService, Depends(get_character_service)],
) -> Any:
    character = character_service.get_character_by_uuid(uuid)

    if not character:
        raise HTTPException(status_code=404, detail=f"Character {uuid} not found")

    return character


@router.get("/character/random", response_model=PaginatedResponse)
def get_random_character(character_service: Annotated[CharacterService, Depends(get_character_service)]) -> Any:
    character = character_service.get_random_character()

    if not character:
        logger.error("Could not get a random character from database")
        raise HTTPException(status_code=500, detail="No data available")

    return paginated_response([character], 0, 0)


@router.get("/houses", response_model=PaginatedResponse)
def get_houses(
    common_query_params: CommonQueryParams,
    house_service: Annotated[HouseService, Depends(get_house_service)],
    status: Annotated[str | None, Query(strict=True, examples=["Major", "major"])] = None,
) -> Any:
    houses = house_service.get_houses(status, common_query_params["limit"], common_query_params["offset"])

    if not houses and status is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, status House {status.capitalize()} does not exist",
        )

    return paginated_response(houses, common_query_params["limit"], common_query_params["offset"])


@router.get("/organisations", response_model=PaginatedResponse)
def get_organisations(
    common_query_params: CommonQueryParams,
    organisation_service: Annotated[OrganisationService, Depends(get_organisation_service)],
) -> Any:
    organisations = organisation_service.get_organisations(common_query_params["limit"], common_query_params["offset"])

    if not organisations:
        raise HTTPException(status_code=404, detail="Items not found")

    return paginated_response(organisations, common_query_params["limit"], common_query_params["offset"])


@router.get("/planet/{uuid}", response_model=Planet)
def get_planet(
    uuid: UUID4,
    planet_service: Annotated[PlanetService, Depends(get_planet_service)],
) -> Any:
    planet = planet_service.get_planet_by_uuid(str(uuid))

    if not planet:
        raise HTTPException(status_code=404, detail=f"Planet {uuid} not found")

    return planet


@router.get("/planets", response_model=PaginatedResponse)
def get_planets(
    common_query_params: CommonQueryParams,
    planet_service: Annotated[PlanetService, Depends(get_planet_service)],
) -> Any:
    planets = planet_service.get_planets(common_query_params["limit"], common_query_params["offset"])

    if not planets:
        raise HTTPException(status_code=404, detail="Items not found")

    return paginated_response(planets, common_query_params["limit"], common_query_params["offset"])
