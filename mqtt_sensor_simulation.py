import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"
port = 1883
topic = "sensor/data"

def simulate_sensor_data():
    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 50.0)
        payload = f'{{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}}'
        client.publish(topic, payload)
        print(f"Published: {payload}")
        time.sleep(1)

client = mqtt.Client()
try:
    client.connect(broker, port)
    print(f"Connected to MQTT broker at {broker}:{port}")
    print(f"Publishing to topic: {topic}")
    print("Press Ctrl+C to stop\n")
    simulate_sensor_data()
except KeyboardInterrupt:
    print("\nStopping MQTT sensor...")
    client.disconnect()
except Exception as e:
    print(f"Error: {e}")
    print("Make sure Mosquitto broker is running!")
