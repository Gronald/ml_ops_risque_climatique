FROM python:3.8

WORKDIR /app

COPY /src /app/src

COPY /models /app/models

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]