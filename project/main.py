from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator
from fastapi import FastAPI
from project.config.base import settings
from project.core.db_connection import database
from project.core.routers import register_routers

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator:
    await database.connect()
    yield
    await database.disconnect()

def setup_logging_context() -> None:
    logging.basicConfig(
        level=settings.LOGGING.LEVEL,
        format=settings.LOGGING.FORMAT,
        datefmt=settings.LOGGING.DATE_FORMAT,
    )


app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    dependencies=[],
    lifespan=lifespan,
)
setup_logging_context()
register_routers(app)

if __name__ == '__main__':
    pass