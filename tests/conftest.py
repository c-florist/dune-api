import pytest

from app.v1.database import DbClient
from app.constants import DB_PATH


@pytest.fixture
def db_client():
    db = DbClient(DB_PATH)
    yield db
    db.close()
