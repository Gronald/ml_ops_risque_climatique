FROM ubuntu:18.04

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install python3-pip -y && pip install -r requirements.txt

RUN mkdir /src/app
WORKDIR /src/app
COPY . /src/app

CMD uvicorn app --reload 
