import boto3
from config.core import config
import joblib
import tempfile

def get_model():
    model_key = f'{config.s3_model_key}/{config.pipeline_save_file}{config.ml_model_version}.{config.ml_model_filetype}'
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket =config.s3_model_bucket , Key =model_key )

    with tempfile.TemporaryFile() as temp_file:
        temp_file.write(response['Body'].read())
        temp_file.seek(0)
        loaded_model = joblib.load(temp_file)

    return loaded_model
