# inference/app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.api.main import api_router


# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Inference API for ML",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/", tags=["Machine Learning"])
def start():
    return {"ML": "Inference API"}

# Include the API router
app.include_router(api_router, prefix=settings.API_V1_STR)