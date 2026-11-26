FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir paho-mqtt

COPY sensor.py .

CMD ["python", "sensor.py"]