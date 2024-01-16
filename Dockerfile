FROM python:3.8

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --upgrade -r /src/requirements.txt

COPY ./src/test_main.py /src/test_main.py

RUN pytest

COPY ./src/main.py /src/main.py
 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]