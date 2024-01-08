FROM ubuntu:18.04

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install python3-pip -y && pip install -r requirements.txt

RUN mkdir /home/app
WORKDIR /home/app
COPY . /home/app

CMD uvicorn app --reload 
