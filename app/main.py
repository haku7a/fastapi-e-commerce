from fastapi import FastAPI
from app.core.config import Settings

settings = Settings()

app = FastAPI()


@app.get("/")
def read_root():
    return {"project": settings.PROJECT_NAME, "api_prefix": settings.API_V1_STR}
