import subprocess

from fastapi import FastAPI

from api.endpoints.gallery import gallery_router


def create_app():
    app = FastAPI()

    app.include_router(gallery_router)

    subprocess.run(["alembic", "upgrade", "head"])

    return app
