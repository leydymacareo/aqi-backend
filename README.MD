# 🌬️ AQI App - Backend

Este es el backend de la aplicación AQI Predictor. Se trata de una API REST desarrollada con FastAPI que recibe variables ambientales y demográficas, y devuelve una predicción sobre la calidad del aire en formato JSON. El modelo de predicción ha sido entrenado previamente y se ejecuta en un servidor remoto.

---

## 🌐 Hosting

### 🔧 Servidor
Alojado en DigitalOcean:

```
http://157.245.140.29:8080
```

Conexión por SSH:

```bash
ssh -i digitalocean root@157.245.140.29
```

### 📂 Ubicación del proyecto

El backend está instalado en:

```
/opt/aqi-app
```

---

## 🚀 Inicio del servidor

Para ejecutar el servidor manualmente:

```bash
cd /opt/aqi-app
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Esto levanta el servicio en la IP pública y puerto 8080 para que sea accesible desde la app móvil o herramientas externas.

---

## 📊 Variables esperadas por el endpoint `/predict`

La API espera recibir un JSON con los siguientes campos:

| Campo                | Tipo   | Descripción |
|----------------------|--------|-------------|
| temperatura          | float  | Temperatura ambiente en grados Celsius |
| humedad              | float  | Porcentaje de humedad relativa del aire |
| pmTotal              | float  | Materia particulada total en µg/m³ |
| no2                  | float  | Concentración de dióxido de nitrógeno (ppb) |
| so2                  | float  | Concentración de dióxido de azufre (ppb) |
| co                   | float  | Concentración de monóxido de carbono (ppm) |
| proximidad           | float  | Proximidad a zonas industriales (km) |
| densidadPoblacional  | float  | Densidad poblacional (personas por km²) |

---

## 📬 Ejemplo de uso con curl

```bash
curl -X POST http://157.245.140.29:8080/predict \
     -H "Content-Type: application/json" \
     -d '{
           "temperatura": 25.5,
           "humedad": 60.0,
           "pmTotal": 45.0,
           "no2": 20.0,
           "so2": 15.0,
           "co": 0.8,
           "proximidad": 1.2,
           "densidadPoblacional": 3500.0
         }'
```

---

## ✅ Respuesta esperada

```json
{
  "prediccion": "Moderate"
}
```

Valores posibles para `"prediccion"`:

- `"Good"` → Aire limpio y seguro
- `"Moderate"` → Aceptable para la mayoría, pero puede afectar a personas sensibles
- `"Poor"` → Calidad dañina para grupos sensibles
- `"Hazardous"` → Calidad peligrosa para toda la población

---

## 📦 Requisitos del proyecto

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- scikit-learn
- joblib

Instalación:

```bash
pip install -r requirements.txt
```

---

## 🛠 Estructura del proyecto

```
aqi-app/
│
├── app/
│   ├── main.py         # Archivo principal con el endpoint
│   ├── model.joblib    # Modelo entrenado (machine learning)
│   └── ...
├── requirements.txt
└── README.md
```

---

## 🤝 Enlace al Frontend

Puedes consultar el repositorio móvil desarrollado en Jetpack Compose aquí:  
➡️ [AQI Predictor - App Android](https://github.com/tu-usuario/aqi-predictor)

---

¿Preguntas? ¿Contribuciones? ¡Bienvenidas!
