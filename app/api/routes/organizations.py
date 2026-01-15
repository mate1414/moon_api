from fastapi import APIRouter, Depends, HTTPException, Query

from app.repository.factory.factory import RepositoryFactory, get_repository_factory
from app.schemas.geo import RadiusSearch
from app.schemas.organization import OrganizationShema
from app.services.organization.service import OrganizationService


router = APIRouter(prefix="/organizations")


@router.get("/{organization_id}", response_model=OrganizationShema)
def get_organization(
    organization_id: int,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> dict[str, str]:
    """
    Получить информацию о организации по 'organization_id'.

    returns:
        dict[str, str]
    """
    organization = repo_factory.organization.get_one(organization_id)

    if not organization:
        raise HTTPException(status_code=404, detail="Not found")

    return OrganizationShema.model_validate(organization).model_dump()


@router.get("/by-building/{building_id}", response_model=list[OrganizationShema])
def get_organizations_by_building(
    building_id: int,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> list[dict[str, str]]:
    """
    Получить список организаций по building_id.

    returns:
        list[dict[str, str]]
    """

    organizations = repo_factory.organization.get_multi_by_building_id(building_id)
    if not organizations:
        raise HTTPException(status_code=404, detail="Not found")

    return [OrganizationShema.model_validate(organization).model_dump() for organization in organizations]


@router.get("/by-map-point/radius", response_model=list[OrganizationShema])
def get_organizations_in_radius(
    search: RadiusSearch,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> list[dict[str, str]]:
    """
    Получить список организаций в заданном радиусе.

    Args:
        search (RadiusSearch): Данные области для поиска.
        repo_factory: Фабрика репозитория

    returns:
        list[dict[str, str]]
    """

    organizations = OrganizationService(repo_factory).get_organizations_by_map_point_in_radius(
        search.latitude,
        search.longitude,
        search.radius_km,
    )

    return [organization.model_dump() for organization in organizations]

@router.get("/by-activity/{activity_id}", response_model=list[OrganizationShema])
def get_organizations_by_activity_recursive(
    activity_id: int,
    max_depth: int = Query(1, ge=1, le=10, description="Максимальная глубина вложенности"),
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> list[dict[str, str]]:
    """
    Получить список организаций с заданной деятельностью.

    Возможно получение организаций, занимающимися подзависимыми дейстельностями, от указанной:

    `/api/organizations/by_activity/1?max_depth=2`
        заданы значения:
            - activity_id = 1
            - max_depth = 2

    returns:
        list[dict[str, str]]
    """

    organizations = repo_factory.organization.get_multi_by_activity_recursive(
        activity_id=activity_id,
        max_depth=max_depth,
    )

    return [OrganizationShema.model_validate(organization).model_dump() for organization in organizations]
