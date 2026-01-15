from fastapi import APIRouter, Depends, HTTPException

from app.repository.factory.factory import RepositoryFactory, get_repository_factory
from app.schemas.building import BuildingSchema
from app.schemas.geo import RadiusSearch
from app.services.building.service import BuildingService


router = APIRouter(prefix="/buildings")


@router.get("/by-map-point/radius", response_model=list[BuildingSchema])
def search_buildings_in_radius(
    search: RadiusSearch,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> list[dict[str, str]]:
    """
    Получить список зданий в заданном радиусе.

    Args:
        search (RadiusSearch): Данные области для поиска.
        repo_factory: Фабрика репозитория

    returns:
        list[dict[str, str]]
    """

    buildings = BuildingService(repo_factory).get_buildings_by_map_point_in_radius(
        search.latitude,
        search.longitude,
        search.radius_km,
    )

    if not buildings:
        raise HTTPException(status_code=404, detail="Not found")

    return [building.model_dump() for building in buildings]
