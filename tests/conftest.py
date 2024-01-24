import pytest

from app.v1.database import DbClient
from app.v1.constants import DB_PATH
from app.v1.utils import run_migrations


@pytest.fixture
def db_client():
    db = DbClient(DB_PATH)

    run_migrations(db)
    yield db

    db.close()
