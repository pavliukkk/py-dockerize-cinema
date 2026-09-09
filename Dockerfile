FROM python:3.10.8-slim
LABEL maintainer = "Pavliuk"

ENV PYTHOUNNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .