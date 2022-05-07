FROM python:3.8-slim-buster

WORKDIR /blenderbot
RUN apt-get update -y
RUN apt-get install -y curl

COPY . /blenderbot

RUN pip3 install -r requirements.txt

CMD [ "python3", "./run.py"]


