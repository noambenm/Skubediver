FROM python:3.12-alpine3.20

RUN addgroup -S python && adduser -S python -G python

WORKDIR /app

COPY requirerments.txt .

RUN pip install -r requirerments.txt

COPY app.py .

USER python

ENTRYPOINT [ "python3", "app.py" ]