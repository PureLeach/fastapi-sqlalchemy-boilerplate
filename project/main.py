from fastapi import FastAPI
from project.config.base import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
    dependencies=[],
    lifespan=None,
)


if __name__ == '__main__':
    pass