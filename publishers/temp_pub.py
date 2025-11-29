import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
STUDENT_ID = "12112662"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    temp = random.randint(20, 35)
    msg = f"Temp={temp} | ID={STUDENT_ID}"
    client.publish("lab/temperature", msg)
    print("[PUBLISHER] Sent:", msg)
    time.sleep(2)
