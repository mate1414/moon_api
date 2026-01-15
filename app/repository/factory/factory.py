from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repository.building import BuildingRepository
from app.repository.organization import OrganizationRepository


class RepositoryFactory:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    @property
    def organization(self) -> OrganizationRepository:
        return OrganizationRepository(self.db_session)

    @property
    def building(self) -> BuildingRepository:
        return BuildingRepository(self.db_session)


def get_repository_factory(db: Session = Depends(get_db)) -> RepositoryFactory:
    return RepositoryFactory(db)
