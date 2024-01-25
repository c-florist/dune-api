from contextlib import closing

from app.v1.database import DbClient
from app.constants import DB_PATH
from app.utils import run_migrations
from .seed_data import CHARACTERS, HOUSES


def drop_test_db() -> None:
    db_client = DbClient(DB_PATH, mode="rw")

    with closing(db_client.conn.cursor()) as cursor:
        cursor.executescript(
            """
            DROP TABLE IF EXISTS character;
            DROP TABLE IF EXISTS house;
            DROP TABLE IF EXISTS organisation;
        """
        )

    db_client.close()


def seed_test_db() -> None:
    db_client = DbClient(DB_PATH, mode="rwc")
    run_migrations(db_client)

    with closing(db_client.conn.cursor()) as cursor:
        cursor.executemany(
            "INSERT INTO house (id, name, homeworld, status, colours, symbol, created_at, updated_at) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            HOUSES,
        )

        cursor.executemany(
            "INSERT INTO character (titles, first_name, last_name, suffix, dob, birthplace, dod, house_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            CHARACTERS,
        )

    db_client.close()
