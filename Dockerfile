FROM  python:3.10.0a7-slim-buster

WORKDIR /app
COPY . .

# Set ENV Variables
ENV FLASK_APP='./src/app.py'
ENV FLASK_ENV='development'

# Get all the requirements
RUN apt update
RUN apt-get install gcc g++ -y
RUN pip3 install --no-cache-dir -r ./requirements.txt 

CMD ["flask", "run", "--host=0.0.0.0"]