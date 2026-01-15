from app.repository.factory.factory import RepositoryFactory
from app.schemas.organization import OrganizationShema
from app.services.building.service import BuildingService


class OrganizationService:

    def __init__(self, repo_factory: RepositoryFactory):
        self.repo_factory = repo_factory

    def get_organizations_by_map_point_in_radius(
        self,
        latitude: float,
        longitude: float,
        radius_km: float,
    ) -> list[OrganizationShema]:
        organizations = self.repo_factory.organization.get_multi()

        organizations_in_radius = []
        for org in organizations:
            org_schema = OrganizationShema.model_validate(org)

            if BuildingService.is_building_in_radius(
                    latitude,
                    longitude,
                    org_schema.building,
                    radius_km,
            ):
                organizations_in_radius.append(org_schema)

        return organizations_in_radius
