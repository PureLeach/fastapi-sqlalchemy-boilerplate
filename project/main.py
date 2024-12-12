from fastapi import FastAPI
from project.config.base import settings
from project.core.db.connection import get_database

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    dependencies=[],
    lifespan=None,
)


if __name__ == '__main__':
    x = get_database().connect()
    print(f'\033[31m x, { x }, {type(x)} \033[0m')
    pass