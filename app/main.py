from fastapi import FastAPI

from .v1.router import router as v1_root_router

app = FastAPI(
    title="Dune API",
    summary="API for information about Frank Herbert's book series Dune",
    version="0.0.1",
    redoc_url=None,
)


@app.get("/")
def root() -> dict[str, dict[str, str]]:
    return {"v1": {"status": "OK"}}


app.include_router(v1_root_router, prefix="/v1")
