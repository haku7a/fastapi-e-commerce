from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router
from contextlib import asynccontextmanager
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"project": settings.PROJECT_NAME, "api_prefix": settings.API_V1_STR}
