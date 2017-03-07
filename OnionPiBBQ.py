__author__ = 'rainsbp'

import requests
import json
import time

cs_pin = 16
clock_pin = 1
data_pin = 15
units = "f"
value = "test"

# from max6675 import MAX6675, MAX6675Error
#
# for i in range(0, 10, 1):
#     thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
#     value = thermocouple.get()
#     thermocouple.cleanup()
#
#     print(value)
#
#     time.sleep(1)

import spidev
import RPiSensors.max6675 as sensor_6675

for i in range(10):
    sensor = sensor_6675.Max6675(0, 0)
    print sensor.temperature
    time.sleep(2)

url = "https://api.onion.io/v1/devices/4e1ad09c-45ec-440b-b3d6-59e811d7bcba/i2c_exp/oled-exp"

payload = json.dumps({
    "command": "set",
    "params": {
        "write": str(value),
        "scroll": "right"
    },
    "option": "i"
}
)
headers = {
    'x-api-key': "LENEg6UrepbJIAgd8ksx9HrX7mbhy1kYNAfGZsPpugcBUfaE1hqtRccIUnruFeKN",
    'content-type': "application/json",
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
