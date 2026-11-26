import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "mosquitto"
PORT = 1883

TOPIC_TEMPERATURA = "casa/sensor/temperatura"
TOPIC_UMIDADE = "casa/sensor/umidade"

client = mqtt.Client()

print("Conectando ao MQTT...")

while True:
    try:
        client.connect(BROKER, PORT, 60)
        break
    except Exception as e:
        print("MQTT ainda não disponível:", e)
        time.sleep(3)

print("Sensor virtual conectado!")

temperatura = 26.0
umidade = 60.0

while True:

    # Simulação normal
    temperatura += random.uniform(-0.5, 0.5)
    umidade += random.uniform(-1.5, 1.5)

    # Limites para manter a simulação razoável
    temperatura = max(20, min(35, temperatura))
    umidade = max(25, min(80, umidade))

    client.publish(TOPIC_TEMPERATURA, round(temperatura, 2))

    client.publish(TOPIC_UMIDADE, round(umidade, 2))

    print(f"Temperatura: {temperatura:.2f} °C | " f"Umidade: {umidade:.2f} %")

    time.sleep(5)
