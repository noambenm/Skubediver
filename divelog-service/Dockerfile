FROM python:3.12-slim

RUN useradd python

WORKDIR /app

COPY requirerments.txt .

RUN pip install -r requirerments.txt

COPY app.py .

USER python

ENTRYPOINT [ "python3", "app.py" ]