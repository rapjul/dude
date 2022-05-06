# FROM mcr.microsoft.com/playwright/python:v1.21.0-focal
FROM python:3.9-slim-buster AS base
ENV PYTHONUNBUFFERED=1

# RUN apt install ca-certificates

WORKDIR /app

# ENV PIP_DEFAULT_TIMEOUT=100 \
#     PIP_DISABLE_PIP_VERSION_CHECK=1 \
#     PIP_NO_CACHE_DIR=1
ENV PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=1

# COPY ./pyproject.toml /
# COPY ./poetry.lock /
# # COPY  *.toml *.lock /
COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir --upgrade poetry && \
  # poetry config virtualenvs.create false && \
  poetry install --no-dev --no-root

WORKDIR /data

VOLUME /data

ARG OUTPUT_FORMAT=json


# CMD dude scrape --parsel --url https://example.com --output "./data/results.${OUTPUT_FORMAT}" ./example.py

# ENTRYPOINT [ "dude", "scrape" ]
# CMD ["--parsel", "--url", "https://example.com", "--output", "./data/results.${OUTPUT_FORMAT}", "./example.com.py"]
