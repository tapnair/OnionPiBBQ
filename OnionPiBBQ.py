__author__ = 'rainsbp'

from max31855.max6675 import MAX6675, MAX6675Error
import requests
import json

cs_pin = 24
clock_pin = 23
data_pin = 22
units = "f"
thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
value = thermocouple.get()
thermocouple.cleanup()


url = "https://api.onion.io/v1/devices/4e1ad09c-45ec-440b-b3d6-59e811d7bcba/i2c_exp/oled-exp"

payload = json.dumps({
    "command": "set",
    "params": {
        "write": value,
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
