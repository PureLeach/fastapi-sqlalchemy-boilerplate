from pydantic_settings import BaseSettings
from project.config.db import DBConfig

class Settings(BaseSettings):
    DEBUG: bool = True
    PROJECT_NAME: str = "fastapi-boilerplate-project"

    DB: DBConfig = DBConfig()



settings = Settings()
