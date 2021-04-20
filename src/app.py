from flask import Flask
import requests
import json

# Contstans
EPS32_IP = "http://192.168.178.35"
ESP32_URL_LED = "/LED"

commands = {
    "on": "0xFFA25D",
    "off": "0xFFE21D",
    "dim": "0xFF629D",
    "bright": "0xFF52AD",
    "multi": "0xFFD1DF",
    "six": "0xFF22DD",
    "red": "0xFF6897",
    "green": "0xFF9867",
    "blue": "0xFFB04F",
    "sun": "0xFF30CF",
    "grass": "0xFF18E7",
    "ocean": "0xFF7A85",
    "wine": "0xFF100xFF",
    "orange": "0xFF38C7",
    "cyan": "0xFF5AA5",
    "purple": "0xFF42BD",
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
            url=url, params={"command": int(commands[command], 0)})
        response = data.text
    except Exception as error:
        response = {"error": error.__str__()}
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
