FROM python:3.8

WORKDIR /src

COPY ./src/requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src/main.py /src/main.py
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]