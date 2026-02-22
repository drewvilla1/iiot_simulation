import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json

data = []

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    data.append((datetime.now(), payload))
    if len(data) > 100:
        data.pop(0)
    
    df = pd.DataFrame(data, columns=["timestamp", "sensor_data"])
    df["temperature"] = df["sensor_data"].apply(lambda x: json.loads(x)["temperature"])
    df["humidity"] = df["sensor_data"].apply(lambda x: json.loads(x)["humidity"])
    
    plt.clf()
    plt.subplot(2, 1, 1)
    plt.plot(df["timestamp"], df["temperature"], 'r-', label="Temperature (°C)")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(df["timestamp"], df["humidity"], 'b-', label="Humidity (%)")
    plt.ylabel("Humidity (%)")
    plt.xlabel("Time")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    client.subscribe("sensor/data")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("localhost", 1883, 60)
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")
    print("Make sure Mosquitto is running!")
    exit(1)

plt.ion()
plt.figure(figsize=(10, 8))
plt.suptitle("Real-Time MQTT Sensor Data")
client.loop_start()

print("Graph is running. Press Ctrl+C in the terminal to stop.")
try:
    plt.show(block=True)
except KeyboardInterrupt:
    print("\nStopping visualization...")
    client.loop_stop()
    client.disconnect()
