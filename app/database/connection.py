from sqlite3 import Connection, DatabaseError, Row, connect
from typing import Type
from types import TracebackType


class DbConnection:
    def __init__(self, file_path: str, mode: str) -> None:
        self.file_path = file_path
        self.mode = mode

    def __enter__(self) -> Connection:
        try:
            self.conn = connect(f"file:{self.file_path}?mode={self.mode}", uri=True)
            self.conn.row_factory = Row
        except DatabaseError as ex:
            raise RuntimeError("Fatal: Unable to connect to database") from ex
        else:
            return self.conn

    def __exit__(
        self,
        exception_type: Type[BaseException] | None,
        exception_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.conn.close()
