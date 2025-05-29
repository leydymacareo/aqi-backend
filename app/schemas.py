from pydantic import BaseModel

class AQIInput(BaseModel):
    temperatura: float
    humedad: float
    pmTotal: float
    no2: float
    so2: float
    co: float
    proximidad: float
    densidadPoblacional: float