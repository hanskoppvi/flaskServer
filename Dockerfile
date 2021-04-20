FROM  python:3.10.0a7-slim-buster

WORKDIR /app
COPY . .
# RUN apk --update add bash nano
# RUN source ./.venv/bin/activate
RUN apt-get update
RUN apt-get -y install gcc 
RUN pip3 install -r requirements.txt 


CMD ["flask", "run", "--host=0.0.0.0"]