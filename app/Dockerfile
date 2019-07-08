FROM python:3.7.3

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y \
    && pip install --upgrade pip \
    && pip install -r requirements.txt