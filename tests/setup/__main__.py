from contextlib import closing
from logging import getLogger

from app.constants import DB_PATH
from app.core.database import DBClient
from app.utils import run_migrations, setup_logging

from .seed_data import CHARACTER_ORGS, CHARACTERS, HOUSES, ORGANISATIONS

logger = getLogger(__name__)


def drop_test_db(db_client: DBClient) -> None:
    with closing(db_client.conn.cursor()) as cursor:
        cursor.executescript(
            """
            DROP TABLE IF EXISTS character_organisation;
            DROP TABLE IF EXISTS character;
            DROP TABLE IF EXISTS house;
            DROP TABLE IF EXISTS organisation;
        """
        )


def seed_test_db(db_client: DBClient) -> None:
    with closing(db_client.conn.cursor()) as cursor:
        cursor.executemany(
            "INSERT INTO house (id, uuid, name, homeworld, status, colours, symbol, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            HOUSES,
        )

        cursor.executemany(
            "INSERT INTO organisation (id, uuid, name, founded, dissolved, misc, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            ORGANISATIONS,
        )

        cursor.executemany(
            "INSERT INTO character (id, uuid, titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, profession, misc, house_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            CHARACTERS,
        )

        cursor.executemany(
            "INSERT INTO character_organisation (character_id, org_id) VALUES (?, ?)",
            CHARACTER_ORGS,
        )


def run() -> None:
    db_client = DBClient(DB_PATH, mode="rwc")

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
