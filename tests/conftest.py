from pathlib import Path
from collections.abc import Generator

import pytest

from app.v1.database.client import DbClient

TESTS_DIR = Path(__file__).parent


def create_schema(db_client):
    # TODO: Replace with app.v1.database.utils:run_migrations()
    schema = TESTS_DIR.parent / Path('app/v1/database/migrations/001.sql')
    sql = schema.read_text()

    with db_client.conn as conn:
        conn.executescript(sql)


@pytest.fixture
def db_client():
    file_path = TESTS_DIR / "test.db"
    db = DbClient(str(file_path), mode="rw")

    create_schema(db)
    yield db

    db.conn.close()
