from fastapi import APIRouter
from app.api.v1.endpoints import health

api_router = APIRouter()

api_router.include_router(health.router, prefix="/system/health", tags=["system"])


@api_router.get("/")
def read_v1_api():
    return {"status": "ok"}
