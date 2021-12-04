# syntax=docker/dockerfile:1
FROM python:3.8.12-slim-buster@sha256:7e732593f25983fa7d4b2d54444be4a785f2397c1cf2f815d2e3638337eee012
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