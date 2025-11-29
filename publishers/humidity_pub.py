import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
STUDENT_ID = "12112662"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    hum = random.randint(30, 90)
    msg = f"Humidity={hum}% | ID={STUDENT_ID}"
    client.publish("lab/humidity", msg)
    print("[PUBLISHER] Sent:", msg)
    time.sleep(2)
