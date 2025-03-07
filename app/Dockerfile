FROM python:3.12-slim-bookworm

RUN apt-get update
RUN apt-get install -y stress
RUN pip install --no-cache-dir uv

ENV UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml .
RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
