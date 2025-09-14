import pytest

from app.core.constants import DB_PATH
from app.core.database import DBClient


@pytest.fixture
def db_client():
    db = DBClient(DB_PATH, mode="rwc")
    yield db
    db.close()
