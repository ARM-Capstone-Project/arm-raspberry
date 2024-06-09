import time
import board
import adafruit_dht
import requests  # Import the requests library for making HTTP calls

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

# URL to send data to (replace with your actual API endpoint)
API_URL = "https://iot-git-myapwint-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/api/readings"

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        # Prepare data as a dictionary (JSON format)
        data = {
            "temperature_f": temperature_f,
            "temperature_c": temperature_c,
            "humidity": humidity
        }

        # Send HTTP POST request
        response = requests.post(API_URL, json=data)

        # Check if the request was successful (optional)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print("Error sending data:", response.status_code)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    # Wait for 60 seconds (1 minute)
    time.sleep(60) 


