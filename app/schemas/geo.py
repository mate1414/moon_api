from pydantic import BaseModel, Field


class RadiusSearch(BaseModel):
    latitude: float = Field(..., description="Широта центра поиска")
    longitude: float = Field(..., description="Долгота центра поиска")
    radius_km: float = Field(..., ge=0, description="Радиус поиска в километрах")
