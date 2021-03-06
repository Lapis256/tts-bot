from os import environ
from fastapi import FastAPI

from route import routers


def create_app():
    app = FastAPI(
        openapi_url=None,
        docs_url=None,
        redoc_url=None
    )
    if environ.get("DEBUG", None) is not None:
        app = FastAPI()

    for router in routers:
        app.include_router(router)

    return app
