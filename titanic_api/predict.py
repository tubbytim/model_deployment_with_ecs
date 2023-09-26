from fastapi import FastAPI
from titanic_api.schemas.data_schemas import InputModel, OutputModel
from titanic_api.get_model import get_model
from titanic_api.config.core import config
from titanic_api.preprocessing import pre_pipeline_preparation
from datetime import datetime
import pandas as pd

app = FastAPI()
titanic_model = get_model()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Define the prediction endpoint
@app.post("/predict", response_model=OutputModel)
async def predict(input: InputModel):
    # Perform the prediction (in this case, we'll square the number)
    pred_data = pd.DataFrame([input.model_dump()])
    preprocessed_pred_data = pre_pipeline_preparation(dataframe=pred_data)
    prediction = titanic_model.predict_proba(preprocessed_pred_data)[0][1]
    
    # Return the prediction result in the specified output schema
    return {"titanic_model_version": config.ml_model_version,
            "timestamp":datetime.now(), 
            "prediction":prediction}
