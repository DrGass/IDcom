import subprocess

from fastapi import FastAPI

from api.endpoints.gallery import gallery_router

def create_app():
    app = FastAPI()

    subprocess.run(["alembic", "upgrade", "head"])

    return app
