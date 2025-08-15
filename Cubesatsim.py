# cubesat_simulation.py
import random
import time
import json

def generate_telemetry():
    """Return a simple telemetry packet as a dict."""
    return {
        "temperature_C": round(random.uniform(20.0, 30.0), 2),  # °C
        "pressure_hPa": round(random.uniform(950.0, 1050.0), 2), # hPa
        "altitude_km": round(random.uniform(400.0, 500.0), 2),   # km (simulated)
        "battery_V": round(random.uniform(3.7, 4.2), 2),         # V
        "rssi_dBm": round(random.uniform(-100.0, -50.0), 2)      # dBm
    }

if __name__ == "__main__":
    print("Starting CubeSat telemetry simulation...\n")
    # Generate 10 telemetry packets (change the range for more/less)
    for _ in range(10):
        packet = generate_telemetry()
        print(json.dumps(packet))   # print JSON line (easy to log or screenshot)
        time.sleep(1)               # 1 second between packets
    print("\nSimulation finished.")
