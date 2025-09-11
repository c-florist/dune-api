from contextlib import asynccontextmanager
from typing import Any

import httpx
from fastapi import FastAPI

from .core.logging import setup_logging
from .response_models import Root
from .v1.router import router as v1
from .v1.services import EnvironmentService


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient() as client:
        app.state.environment_service = EnvironmentService(client)
        yield


setup_logging()
app = FastAPI(
    title="Dune API",
    summary="API for information about the book series Dune by Frank Herbert'",
    version="0.0.1",
    redoc_url=None,
    lifespan=lifespan,
)


@app.get("/", response_model=Root)
def root() -> Any:
    return {"v1": {"status": "active"}}


app.include_router(v1, prefix="/v1")
