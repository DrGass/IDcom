import subprocess

from fastapi import FastAPI

# from api.endpoints import


def create_app():
    app = FastAPI()

    subprocess.run(["alembic", "upgrade", "head"])

    return app
