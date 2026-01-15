from pydantic import BaseModel


class Activity(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
