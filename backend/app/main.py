import subprocess

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from api.endpoints.gallery import gallery_router


def create_app():
    app = FastAPI()
    add_pagination(app)
    app.include_router(gallery_router)

    subprocess.run(["alembic", "upgrade", "head"])

    return app
