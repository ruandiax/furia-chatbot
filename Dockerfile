FROM python:3.10-buster

RUN pip install poetry

WORKDIR /app

COPY . ./

RUN poetry install --no-root