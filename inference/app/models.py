# inference/app/models.py
from pydantic import BaseModel
from typing import List, Dict, Any


class FlightInput(BaseModel):
    carrier: str
    dest: str
    dep_delay: float
    arr_delay: float
    arr_time: float
    month: float
    plane_age: float

class PredictionResponse(BaseModel):
    prediction: float
    probability: List[float]