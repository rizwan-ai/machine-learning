# inference/app/models.py
from pydantic import BaseModel
from typing import List, Dict, Any


class FlightInput(BaseModel):
    carrier: str = "AS"
    dest: str = "HNL"
    dep_delay: float = 5
    arr_delay: float = 5
    arr_time: float = 1505
    month: float = 1
    plane_age: float = 17

class PredictionResponse(BaseModel):
    prediction: float
    probability: List[float]