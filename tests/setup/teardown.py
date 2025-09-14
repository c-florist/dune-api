from sqlite3 import Connection


def teardown_annotations(db_conn: Connection) -> None:
    db_conn.execute("DELETE FROM annotations")
    db_conn.commit()
