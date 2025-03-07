FROM python:3.12-slim-bookworm

RUN pip install --no-cache-dir uv

ENV UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml ./
RUN uv sync

COPY . .

EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
