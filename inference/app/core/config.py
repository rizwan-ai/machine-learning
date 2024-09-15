# inference/app/core/config.py
import os


class Settings:
    PROJECT_NAME: str = "Machine Learning Inference API"
    API_V1_STR: str = "/api/v1"

    # Define the base path where 'notebooks' and artifacts are stored
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    # Path to the 'model-artifacts' inside the notebooks folder
    NOTEBOOKS_DIR: str = os.path.join(BASE_DIR, "..", "notebooks", "notebooks-01", "model-artifacts-01")

    # Model paths
    MODEL_PATH: str = os.path.join(NOTEBOOKS_DIR, "fitted_pipeline_model")
    CV_MODEL_PATH: str = os.path.join(NOTEBOOKS_DIR, "cv_model")

settings = Settings()