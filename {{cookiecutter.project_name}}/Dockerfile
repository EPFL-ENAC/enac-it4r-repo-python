FROM python:3.11-slim


WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends

RUN python3 -m venv /opt/venv

COPY pyproject.toml ./

COPY {{cookiecutter.project_name}}/ /app

RUN pip install .[dev]

