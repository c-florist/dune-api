from contextlib import contextmanager
from pathlib import Path
from sqlite3 import Connection, DatabaseError, connect


@contextmanager
def db_connection(path: Path) -> Connection:
    try:
        conn = connect(f'file:{path}?mode=ro', uri=True)
        yield conn
        conn.close()
    except DatabaseError as ex:
        raise RuntimeError('Fatal: Unable to connect to database') from ex
