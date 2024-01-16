from pathlib import Path

import pytest

from app.v1.database.client import DbClient

ROOT_DIR = Path(__file__).parent.parent


def create_schema(db_client):
    # TODO: Replace with app.v1.database.utils:run_migrations()
    schema = ROOT_DIR / Path("app/v1/database/migrations/001.sql")
    sql = schema.read_text()

    with db_client.conn as conn:
        conn.executescript(sql)


@pytest.fixture
def db_client():
    db = DbClient("test", mode="memory")

    create_schema(db)
    yield db

    db.conn.close()
