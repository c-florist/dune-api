from pathlib import Path
from contextlib import closing

import pytest

from app.v1.database import DbConnection


@pytest.fixture
def db_connection():
    schema = Path(__file__).parent.parent.parent / Path('app/v1/schema.sql')
    schema_sql = schema.read_text()

    with DbConnection('test', mode='memory') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.executescript(schema_sql)

        yield conn
