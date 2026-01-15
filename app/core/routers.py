from fastapi import FastAPI

from app.api.routes import buildings, organizations


def add_routers(app: FastAPI) -> None:
    app.include_router(organizations.router, prefix="/api", tags=["organizations"])
    app.include_router(buildings.router, prefix="/api", tags=["buildings"])
