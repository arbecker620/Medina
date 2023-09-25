FROM python:3.8-slim-buster

WORKDIR /app

COPY /OCR/ /app/OCR


WORKDIR /app/OCR/
RUN pip3 install -r requirements.txt

COPY . .