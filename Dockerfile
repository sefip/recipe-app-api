FROM python:3.6-alpine
MAINTAINER Sefi Piscon

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
copy ./app /app

RUN adduser -D user
USER user
