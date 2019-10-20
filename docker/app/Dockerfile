FROM python:3.7.4

ARG requirements=prod

COPY ./docker/app/requirements /requirements
WORKDIR /requirements
RUN pip install -r ./${requirements}.txt

RUN mkdir -p /src/quickstart
WORKDIR /src/quickstart

EXPOSE 8080
