FROM  python:3.8-alpine

WORKDIR /app
COPY . .

# Set ENV Variables
ENV FLASK_APP='./src/app.py'
ENV FLASK_ENV='development'

# Get all the requierements
RUN apk add gcc g++\
    && pip3 install --no-cache-dir -r ./requirements.txt 

CMD ["flask", "run", "--host=0.0.0.0"]