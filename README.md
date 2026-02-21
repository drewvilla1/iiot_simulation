# iiot_simulation
Simulation of an IIoT sensor network using MQTT, CoAP, and OPC UA protocols with real-time MQTT data visualization (Lab 04 - ITAI 3377)
# Lab 04: Conceptual Design of an IIoT Sensor Network

**Course:** ITAI 3377  
**Team Members:** Andrew Kuruvilla, Marques Roverson, Ruben Valenzuela Alvarado, Ezra Bakatubia  
**Submission Identifier:** A04_EzraBakatubiaGroup2_ITAI_3377 (or L04_AndrewKuruvilla_Group2_ITAI_3377)  
**Date:** February 2026

This repository contains a Python-based simulation of an Industrial Internet of Things (IIoT) sensor network. The project generates realistic temperature and humidity data every second using three key protocols — **MQTT**, **CoAP**, and **OPC UA** — and includes real-time visualization for MQTT data using Matplotlib and Pandas.

## Project Overview

- Simulates sensor data publication (MQTT), observable resource (CoAP client-style POST), and server variable updates (OPC UA)
- Implements improved versions with error handling, logging, and graceful shutdown
- Provides live plotting of MQTT data with rolling buffer
- Includes protocol comparison report and evidence screenshots

## Project Structure
├── README.md

├── mqtt_sensor_simulation.py

├── coap_sensor_simulation.py

├── opcua_sensor_simulation.py

├── data_visualization.py

├── visualizations/

│   ├── mqtt_visualization.png

│   ├── coap_visualization.png

│   ├── opcua_visualization.png

│   └── visualization_demo.mp4

└── comparison_report.pdf
