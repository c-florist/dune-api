from pathlib import Path

import pytest

from app.v1.database import DbClient
from app.v1.utils import run_migrations

ROOT_DIR = Path(__file__).parent.parent


@pytest.fixture
def db_client():
    db = DbClient("test", mode="memory")

    run_migrations(db)
    yield db

    db.conn.close()
