# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN groupadd --gid $GID django && useradd --uid $UID --gid django --shell /bin/bash --create-home django

USER django

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

# TODO: python manage.py migrate