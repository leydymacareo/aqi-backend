from .model_loader import model, scaler, label_encoder
import numpy as np

def predict_aqi(data: list):
    scaled = scaler.transform([data])
    prediction = model.predict(scaled)
    label = label_encoder.inverse_transform(prediction)
    return label[0]
