from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import timedelta
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"

class Settings(BaseSettings):
    SECRET_KEY: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DEBUG: bool

    @property
    def database_url(self) -> str:
        return (f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
                f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}")

    model_config = SettingsConfigDict(env_file=str(env_path))

settings = Settings()
