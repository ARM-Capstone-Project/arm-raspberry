# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
import requests  # Import the requests library for making HTTP calls
# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT22(board.D18)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

# URL to send data to (replace with your actual API endpoint)
API_URL = "https://iot-git-myapwint-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/api/readings"

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )


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
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
