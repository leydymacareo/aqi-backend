from fastapi import FastAPI
from .schemas import AQIInput
from .predictor import predict_aqi
from . import firebase

# Inicializar FastAPI
app = FastAPI()

@app.post("/predict")
def predict_air_quality(input: AQIInput):
    data = list(input.dict().values())
    prediction = predict_aqi(data)


    return {"prediccion": prediction}