FROM python:3.8

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --upgrade -r /src/requirements.txt

EXPOSE 80

COPY ./src /src/
 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]