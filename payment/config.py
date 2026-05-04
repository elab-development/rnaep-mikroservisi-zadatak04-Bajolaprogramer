from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""

    # Inventory service
    INVENTORY_HOST: str = "localhost"
    INVENTORY_PORT: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()