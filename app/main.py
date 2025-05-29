from fastapi import FastAPI
from .schemas import AQIInput
from .predictor import predict_aqi
from . import firebase

# Inicializar FastAPI
app = FastAPI()

@app.post("/predict")
def predict_air_quality(input: AQIInput):
    data = [
        input.temperatura,
        input.humedad,
        input.no2,
        input.so2,
        input.co,
        input.proximidad,
        input.densidadPoblacional,
        input.pmTotal
    ]
    print(data)
    prediction = predict_aqi(data)


    return {"prediccion": prediction}