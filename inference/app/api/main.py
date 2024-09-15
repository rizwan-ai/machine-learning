# inference/app/api/main.py
from fastapi import APIRouter
from app.api.routes import flight


api_router = APIRouter()

# Include flight prediction routes
api_router.include_router(flight.router, prefix="/flight", tags=["Flight API"])