FROM python:3.13-slim

ARG DBMATE_VERSION=v2.28.0
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/download/${DBMATE_VERSION}/dbmate-linux-amd64 && \
    chmod +x /usr/local/bin/dbmate

RUN useradd -m -d /home/appuser appuser
USER appuser
WORKDIR /app

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1                  \
    PYTHONDONTWRITEBYTECODE=1           \
    DB_PATH=/app/dune.sqlite3           \
    DATABASE_URL=sqlite3:/app/dune.sqlite3

RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY --chown=appuser . .

RUN dbmate up && python -m scripts.seed_database

EXPOSE 8080
CMD [ "uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--forwarded-allow-ips", "*" ]
