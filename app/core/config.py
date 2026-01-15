from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "dev"
    STATIC_API_KEY: str = "dev"

    APP_NAME: str = "Organizations"
    APP_DESCRIPTION: str = "Organizations API"

    SQLALCHEMY_DATABASE_URL: str = "postgres://postgres:postgres@localhost:5432/postgres"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
