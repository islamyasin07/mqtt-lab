# MQTT Lab - Mosquitto + Paho
### Student ID: 122xxxxx

## 📌 Description
This lab demonstrates basic MQTT communication using:
- Mosquitto Broker
- Paho MQTT client (Python)
- Multiple Publishers (Temperature, Humidity, People Counter)
- Multiple Subscribers, each listening to a topic

## 📡 Topics Used
- lab/temperature
- lab/humidity
- lab/people

## ▶️ How to Run
1. Start Mosquitto Broker:
- `mosquitto -v`
2. Run Publishers:
- `python publishers/temp_pub.py`
- `python publishers/humidity_pub.py`
- `python publishers/people_pub.py`
3. Run Subscribers:
- `python subscribers/temp_sub.py`
- `python subscribers/humidity_sub.py`
- `python subscribers/people_sub.py`

## 📸 Screenshots
Screenshots included in `/screenshots` folder showing:
- Publisher logs
- Each Subscriber receiving messages
- Student ID included in all messages


