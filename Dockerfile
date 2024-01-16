FROM python:3.8

WORKDIR /app

COPY /src /app/src

COPY /models /app/models

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]