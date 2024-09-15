# inference/app/api/routes/flight.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models import FlightInput, PredictionResponse
from app.services import prediction


# Initialize router
router = APIRouter()

@router.post("/predict")
async def predict_flight(input_data: List[FlightInput]):
    try:
        # Convert input data to list of dicts for the service function
        input_data_list = [data.dict() for data in input_data]
        
        # Get predictions
        results = prediction.predict_flight_delay(input_data_list)
        
        # Format the results according to PredictionResponse model
        formatted_results = [
            PredictionResponse(
                prediction=result['prediction'],
                probability=result['probability']
            )
            for result in results
        ]

        return {"predictions": formatted_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))