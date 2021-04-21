from flask import Flask
import requests
import json

# Contstans
LOCAL_NETWORK = "http://192.168.178."
ESP32_MESSAGE = "hello from esp32!"

# Get the ESP32's IP address
address = 0  # Default
for x in range(256):
    response = ""
    try:
        data = requests.get(
            url=LOCAL_NETWORK + str(x), timeout=0.1)
        response = data.text
    except Exception as error:
        response = ""
    if response == ESP32_MESSAGE:
        address = x
        break

EPS32_IP = LOCAL_NETWORK + str(address)
ESP32_URL_LED = "/LED"

ESP32_COMMANDS = {
    "on": "0xFFA25D",
    "off": "0xFFE21D",
    "dim": "0xFF629D",
    "bright": "0xFF52AD",
    "multi": "0xFFE01F",
    "six": "0xFF22DD",
    "red": "0xFF6897",
    "green": "0xFF9867",
    "blue": "0xFFB04F",
    "sun": "0xFF30CF",
    "grass": "0xFF18E7",
    "ocean": "0xFF7A85",
    "purple": "0xFF10EF",
    "orange": "0xFF38C7",
    "cyan": "0xFF5AA5",
    "magenta": "0xFF42BD",
    "yellow": "0xFF4AB5",
    "up": "0xFFA857",
    "down": "0xFF906F",
}


# Setup
app = Flask(__name__)

# Routes


@app.route('/')
def index():
    return "Hello!"


@app.route('/LED')
def hanldeLED():
    return {"message": "Send a command"}


@app.route('/LED/<command>')
def sendCommand(command):
    response = {}
    url = EPS32_IP + ESP32_URL_LED
    try:
        data = requests.get(
            url=url, params={"command": int(ESP32_COMMANDS[command], 0)})
        response = data.text
    except Exception as error:
        response = {"error": error.__str__()}
    return response
