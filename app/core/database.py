from logging import getLogger
from pathlib import Path
from sqlite3 import Cursor, DatabaseError, connect
from typing import Any

MIGRATIONS_DIR = Path(__file__).parent.parent / "migrations"
logger = getLogger(__name__)


class DBClient:
    def __init__(self, file_path: str, mode: str = "ro") -> None:
        self.file_path = file_path
        self.mode = mode

        try:
            self.conn = connect(
                f"file:{self.file_path}?mode={self.mode}",
                uri=True,
                isolation_level=None,
                check_same_thread=False,
            )
            self.conn.row_factory = self.dict_row_factory
            self.conn.execute("PRAGMA foreign_keys = ON;")
        except DatabaseError as ex:
            raise RuntimeError("Fatal: Unable to connect to database") from ex

    def close(self) -> None:
        self.conn.commit()
        self.conn.close()

    @staticmethod
    def dict_row_factory(cursor: Cursor, row: tuple[Any, ...]) -> dict[str, Any]:
        fields = [column[0] for column in cursor.description]
        return {k: v for k, v in zip(fields, row, strict=False)}
