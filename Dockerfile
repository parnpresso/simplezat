FROM python:3.7.1-alpine

LABEL maintainer="Parn"

ENV APPLICATION_ROOT /app
RUN mkdir $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

COPY Pipfile $APPLICATION_ROOT
COPY Pipfile.lock $APPLICATION_ROOT

RUN pip3 install pipenv
RUN pipenv install --dev

EXPOSE 8000
