# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN groupadd --gid $GID django && useradd --uid $UID --gid django --shell /bin/bash --create-home django

RUN mkdir -p /var/www/html

RUN chown -R django:django /var/www/html
RUN chmod -R 777 /var/www/html

WORKDIR /var/www/html

COPY requirements.txt /var/www/html/
RUN pip install -r requirements.txt
COPY . /var/www/html/

USER django