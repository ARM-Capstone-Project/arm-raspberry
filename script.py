# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import paho.mqtt.client as mqtt
import ssl
import json
import _thread
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT22(board.D18)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='./rootCA.pem', certfile='./certificate.pem.crt', keyfile='./private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("alylqcewl13i8-ats.iot.ap-southeast-1.amazonaws.com", 8883, 60)

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
def publishData(txt):
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
            data = {
            "temperature_f": temperature_f,
            "temperature_c": temperature_c,
            "humidity": humidity
            }

            client.publish("myapi/data", payload=json.dumps({"msg": data}), qos=0, retain=False)

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(2.0)

_thread.start_new_thread(publishData,("Spin-up new Thread...",))

client.loop_forever()
