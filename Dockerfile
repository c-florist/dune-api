FROM python:3.13-slim

RUN useradd -m -d /home/appuser appuser
USER appuser
WORKDIR /app

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1                  \
    PYTHONDONTWRITEBYTECODE=1           \
    DB_PATH=/app/dune.sqlite3

RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY --chown=appuser . .

RUN python -m scripts.seed_database

EXPOSE 8080
CMD [ "uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--forwarded-allow-ips", "*" ]
