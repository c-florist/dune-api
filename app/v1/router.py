from logging import getLogger
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse
from pydantic import UUID4

from app.core.responses import paginated_response
from app.domain.models import Annotation, Character, Planet
from app.services.annotation_service import AnnotationService
from app.services.character_service import CharacterService
from app.services.geospatial_service import GeoSpatialService
from app.services.house_service import HouseService
from app.services.organisation_service import OrganisationService
from app.services.planet_service import PlanetService

from .dependencies import (
    CommonQueryParams,
    get_annotation_service,
    get_character_service,
    get_geospatial_service,
    get_house_service,
    get_organisation_service,
    get_planet_service,
)
from .request_models import AnnotationCreate, AnnotationUpdate, Coordinates
from .response_models import BoolResponse, PaginatedResponse

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


@router.get("/characters/search", response_model=PaginatedResponse)
def search_characters(
    common_query_params: CommonQueryParams,
    character_service: Annotated[CharacterService, Depends(get_character_service)],
    q: str,
) -> Any:
    characters = character_service.search_characters(q, common_query_params["limit"], common_query_params["offset"])

    if not characters:
        raise HTTPException(
            status_code=404,
            detail=f"No characters found matching '{q}'",
        )

    return paginated_response(characters, common_query_params["limit"], common_query_params["offset"])


@router.get("/character/{uuid}")
def get_character(
    uuid: str,
    character_service: Annotated[CharacterService, Depends(get_character_service)],
) -> Character:
    character = character_service.get_character_by_uuid(uuid)

    if not character:
        raise HTTPException(status_code=404, detail=f"Character {uuid} not found")

    return character


@router.get("/character/random")
def get_random_character(character_service: Annotated[CharacterService, Depends(get_character_service)]) -> Character:
    character = character_service.get_random_character()

    if not character:
        logger.error("Could not get a random character from database")
        raise HTTPException(status_code=500, detail="No data available")

    return character


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


@router.get("/houses/search", response_model=PaginatedResponse)
def search_houses(
    common_query_params: CommonQueryParams,
    house_service: Annotated[HouseService, Depends(get_house_service)],
    q: str,
) -> Any:
    houses = house_service.search_houses(q, common_query_params["limit"], common_query_params["offset"])

    if not houses:
        raise HTTPException(
            status_code=404,
            detail=f"No houses found matching '{q}'",
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


@router.get("/planet/{uuid}")
def get_planet(
    uuid: UUID4,
    planet_service: Annotated[PlanetService, Depends(get_planet_service)],
) -> Planet:
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


@router.post("/planet/locate")
async def get_planet_by_coords(
    coordinates: Coordinates,
    planet_service: Annotated[PlanetService, Depends(get_planet_service)],
    geospatial_service: Annotated[GeoSpatialService, Depends(get_geospatial_service)],
) -> Planet:
    environment = await geospatial_service.get_environment_from_coords(coordinates.latitude, coordinates.longitude)
    planet = planet_service.get_planet_by_environment(environment)

    if not planet:
        raise HTTPException(status_code=404, detail=f"No planet found with environment similar to '{environment}'")

    return planet


@router.post("/character/{uuid}/annotation", status_code=201)
def create_character_annotation(
    uuid: str,
    annotation_data: AnnotationCreate,
    annotation_service: Annotated[AnnotationService, Depends(get_annotation_service)],
) -> Annotation:
    return annotation_service.create_annotation("character", uuid, annotation_data)


@router.get("/users/{user_id}/annotations", response_model=PaginatedResponse)
def get_user_annotations(
    user_id: str,
    common_query_params: CommonQueryParams,
    annotation_service: Annotated[AnnotationService, Depends(get_annotation_service)],
) -> Any:
    annotations = annotation_service.get_annotations_for_user(user_id)

    if not annotations:
        raise HTTPException(status_code=404, detail="No annotations found for user")

    return paginated_response(annotations, common_query_params["limit"], common_query_params["offset"])


@router.put("/annotations/{uuid}")
def update_annotation(
    uuid: str,
    user_id: str,
    annotation_data: AnnotationUpdate,
    annotation_service: Annotated[AnnotationService, Depends(get_annotation_service)],
) -> BoolResponse:
    success = annotation_service.update_annotation(uuid, user_id, annotation_data)
    if not success:
        raise HTTPException(status_code=404, detail="Annotation not found or user does not have permission to update")

    return BoolResponse(success=True)


@router.delete("/annotations/{uuid}")
def delete_annotation(
    uuid: str,
    user_id: str,
    annotation_service: Annotated[AnnotationService, Depends(get_annotation_service)],
) -> BoolResponse:
    success = annotation_service.delete_annotation(uuid, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Annotation not found or user does not have permission to delete")

    return BoolResponse(success=True)
