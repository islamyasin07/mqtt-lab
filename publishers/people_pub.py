import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
STUDENT_ID = "12112662"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    ppl = random.randint(0, 20)
    msg = f"People={ppl} | ID={STUDENT_ID}"
    client.publish("lab/people", msg)
    print("[PUBLISHER] Sent:", msg)
    time.sleep(2)
