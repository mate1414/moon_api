from pydantic import BaseModel

from app.schemas.activity import Activity
from app.schemas.building import BuildingSchema


class OrganizationPhone(BaseModel):
    phone_number: str

    class Config:
        from_attributes = True


class OrganizationShema(BaseModel):
    id: int
    name: str
    building: BuildingSchema
    phone_numbers: list[OrganizationPhone]
    activities: list[Activity]

    class Config:
        from_attributes = True
