from sqlalchemy.orm import Session

from app.db.models.building import Building
from app.repository.repository import BaseRepository


class BuildingRepository(BaseRepository):
    """
    Репозиторий для получения записей из таблицы 'buildings'
    """

    def __init__(self, db: Session):
        super().__init__(Building, db)

    def get_multi(self) -> list[Building]:
        return self.db.query(self.model).all()
