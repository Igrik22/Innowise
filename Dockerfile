FROM python:3.9

WORKDIR /innowise

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /innowise

RUN pip install -r /innowise/requirements.txt

COPY . /innowise

EXPOSE 8000