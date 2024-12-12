from databases import Database, DatabaseURL
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from project.core.db.helpers import metadata, connection_init
from project.config.base import settings


f = settings.DB.DATABASE_DSN
print(f'\033[31m f, { f }, {type(f)} \033[0m')

database_url = DatabaseURL(settings.DB.DATABASE_DSN)
database = Database(database_url, server_settings={'jit': 'off'}, init=connection_init)
print(f'\033[31m database, { database }, {type(database)} \033[0m')
engine = create_async_engine(settings.DB.DATABASE_DSN, echo=True)


def get_database() -> Database:
    return database