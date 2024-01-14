import pytest

from app.v1.database import DbConnection


@pytest.fixture
def db_connection():
    yield DbConnection(file_path="test", mode="memory")


def test_db_connection_success(db_connection):
    with db_connection as conn:
        result = conn.execute('SELECT "Bananas" AS test')
        row = result.fetchone()

    assert row[0] == "Bananas"
