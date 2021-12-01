FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /code

WORKDIR /code

RUN pip install -r /code/requirements.txt
RUN flake8 --ignore=E501,F401 /code

