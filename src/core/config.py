from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "IMAGE HANDLER V1"


settings = Settings()
