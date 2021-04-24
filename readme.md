# Flask server to control my SmartHouse

## Requirements

Create two enviroment variables

> $env:FLASK_APP='app.py'
> $env:FLASK_ENV='development'

## IR LED

This route is use to control de LED with the IR transmitter.

Example URL:
http://192.168.178.30:5000/LED/off

## Docker

To build the Docker container use

> docker build -t testing-flask .

And to run it use:

> docker run -p 5000:5000 testing-flask
