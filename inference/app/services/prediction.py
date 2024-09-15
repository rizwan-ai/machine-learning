# inference/app/services/prediction.py
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.ml import PipelineModel
from pyspark.ml.tuning import CrossValidatorModel
from app.core.config import settings
import os


# Initialize Spark session
spark = SparkSession.builder \
    .appName("FlightDelayInference") \
    .master("local[*]") \
    .getOrCreate()

# Load the trained pipeline model and cross-validated model
pipeline_model_path = settings.MODEL_PATH
cv_model_path = settings.CV_MODEL_PATH

# Check if the paths are valid
if not os.path.exists(pipeline_model_path):
    raise FileNotFoundError(f"Pipeline model not found at {pipeline_model_path}")
if not os.path.exists(cv_model_path):
    raise FileNotFoundError(f"Cross-validator model not found at {cv_model_path}")

# Load models (only once at startup)
pipeline_model = PipelineModel.load(pipeline_model_path)
cv_model = CrossValidatorModel.load(cv_model_path)

# Define schema for the input data
schema = StructType([
    StructField("carrier", StringType(), True),
    StructField("dest", StringType(), True),
    StructField("dep_delay", DoubleType(), True),
    StructField("arr_delay", DoubleType(), True),
    StructField("arr_time", DoubleType(), True),
    StructField("month", DoubleType(), True),
    StructField("plane_age", DoubleType(), True)
])

def predict_flight_delay(input_data_list):
    """
    Function to predict if flights will be delayed or not based on input features.
    """
    # Create a Spark DataFrame from the list of input data
    input_df = spark.createDataFrame(input_data_list, schema)

    # Transform input data using the pipeline model
    transformed_df = pipeline_model.transform(input_df)

    # Make predictions using the cross-validated model
    predictions = cv_model.transform(transformed_df)

    # Collect and convert results to a JSON-serializable format
    results = predictions.select("prediction", "probability").collect()

    # Convert to a list of dictionaries
    results_dict = [dict(row.asDict()) for row in results]

    # # Debugging: print the results to check
    # print("Results ----- :", results_dict)

    return results_dict    