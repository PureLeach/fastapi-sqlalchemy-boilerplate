import ssl
from enum import Enum
from pathlib import Path
from ssl import SSLContext
from urllib.parse import quote

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings

from pydantic import PostgresDsn, field_validator


class DBConfig(BaseSettings):
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_HOST: str = ""
    POSTGRES_PORT: int = 5432
    POSTGRES_DB_NAME: str = ""
    
    DATABASE_DSN: str = ""

    @field_validator('DATABASE_DSN', mode='before')
    @classmethod
    def assemble_db_uri(cls, _: str | None, values: ValidationInfo) -> str:
        return str(
            PostgresDsn.build(
                scheme='postgresql+asyncpg',
                username=values.data['POSTGRES_USER'],
                password=quote(values.data['POSTGRES_PASSWORD']),
                host=values.data['POSTGRES_HOST'],
                port=values.data['POSTGRES_PORT'],
                path=f'{values.data["POSTGRES_DB_NAME"]}',
            )
        )
