# AQI App

## Hosting

### Server
Hosted on DigitalOcean: 157.245.140.29

```shell
ssh -i digitalocean root@157.245.140.29
```

### Startup

Located and installed in /opt/aqi-app
Start using uvicorn

```shell
cd /opt/aqi-app
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

### Access
http://157.245.140.29:8080/predict

```shell

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