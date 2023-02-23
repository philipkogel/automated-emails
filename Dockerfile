FROM python:3.10-alpine
LABEL maintainer="philipkogel"

COPY ./app /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
