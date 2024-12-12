from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    PROJECT_NAME: str = "boilerplate-project"


settings = Settings()
