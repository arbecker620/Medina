FROM python:3.8-slim-buster

WORKDIR /app

COPY /File/ /app/File

WORKDIR /app/File/
RUN pip3 install -r requirements.txt

COPY . .