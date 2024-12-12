from databases import Database, DatabaseURL
from sqlalchemy.ext.asyncio import create_async_engine
from project.core.helpers.db import connection_init
from project.config.base import settings

from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s',
    }
)

database_url = DatabaseURL(settings.DB.DATABASE_DSN)
database = Database(database_url, server_settings={'jit': 'off'}, init=connection_init)
engine = create_async_engine(settings.DB.DATABASE_DSN, echo=True)
