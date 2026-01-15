from app.repository.factory.factory import RepositoryFactory
from app.schemas.building import BuildingSchema
from app.services.utils import calculate_distance


class BuildingService:

    def __init__(self, repo_factory: RepositoryFactory):
        self.repo_factory = repo_factory

    @classmethod
    def is_building_in_radius(
            cls,
            latitude: float,
            longitude: float,
            building: BuildingSchema,
            radius_km: float,
    ) -> bool:
        distance = calculate_distance(latitude, longitude, building.latitude, building.longitude)

        if distance <= radius_km:
            return True

        return False

    def get_buildings_by_map_point_in_radius(
        self,
        latitude: float,
        longitude: float,
        radius_km: float,
    ) -> list[BuildingSchema]:
        buildings = self.repo_factory.building.get_multi()

        buildings_in_radius = []
        for building in buildings:
            building_schema = BuildingSchema.model_validate(building)

            if self.is_building_in_radius(latitude, longitude, building_schema, radius_km):
                buildings_in_radius.append(building_schema)

        return buildings_in_radius
