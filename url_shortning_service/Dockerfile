
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /url_shortner_service

WORKDIR /url_shortner_service

ADD . /url_shortner_service/

RUN pip install -r requirements.txt
