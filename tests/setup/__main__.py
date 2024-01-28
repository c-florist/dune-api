from logging import getLogger
from contextlib import closing

from app.v1.database import DbClient
from app.constants import DB_PATH
from app.utils import run_migrations, setup_logging
from .seed_data import CHARACTERS, HOUSES, ORGANISATIONS

logger = getLogger(__name__)


def drop_test_db(db_client: DbClient) -> None:
    with closing(db_client.conn.cursor()) as cursor:
        cursor.executescript(
            """
            DROP TABLE IF EXISTS character;
            DROP TABLE IF EXISTS house;
            DROP TABLE IF EXISTS organisation;
        """
        )


def seed_test_db(db_client: DbClient) -> None:
    with closing(db_client.conn.cursor()) as cursor:
        cursor.executemany(
            "INSERT INTO house (id, name, homeworld, status, colours, symbol, created_at, updated_at) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
            HOUSES,
        )

        cursor.executemany(
            "INSERT INTO character (titles, first_name, last_name, suffix, dob, birthplace, dod, house_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            CHARACTERS,
        )

        cursor.executemany(
            "INSERT INTO organisation (id, name, founded, dissolved, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
            ORGANISATIONS,
        )


def run() -> None:
    db_client = DbClient(DB_PATH, mode="rwc")

    logger.info("Dropping database tables ...")
    drop_test_db(db_client)

    logger.info("Running migrations ...")
    run_migrations(db_client)

    logger.info(f"Seeding test database at {DB_PATH} ...")
    seed_test_db(db_client)

    db_client.close()


if __name__ == "__main__":
    setup_logging()
    run()
