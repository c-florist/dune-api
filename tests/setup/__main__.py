import subprocess
from contextlib import closing
from logging import getLogger
from pathlib import Path

from app.core.constants import DB_PATH
from app.core.database import DBClient
from app.core.logging import setup_logging

from .seed_data import CHARACTER_ORGS, CHARACTERS, HOUSES, ORGANISATIONS, PLANETS

logger = getLogger(__name__)


def seed_test_db(db_client: DBClient) -> None:
    with closing(db_client.conn.cursor()) as cursor:
        cursor.executemany(
            "INSERT INTO house (id, uuid, name, homeworld, status, colours, symbol) VALUES (?, ?, ?, ?, ?, ?, ?)",
            HOUSES,
        )

        cursor.executemany(
            "INSERT INTO organisation (id, uuid, name, founded, dissolved, misc) VALUES (?, ?, ?, ?, ?, ?)",
            ORGANISATIONS,
        )

        cursor.executemany(
            "INSERT INTO character (id, uuid, titles, aliases, first_name, last_name, suffix, dob, birthplace, dod, profession, misc, house_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            CHARACTERS,
        )

        cursor.executemany(
            "INSERT INTO character_organisation (character_id, org_id) VALUES (?, ?)",
            CHARACTER_ORGS,
        )

        cursor.executemany(
            "INSERT INTO planet (id, uuid, name, environment, ruler) VALUES (?, ?, ?, ?, ?)",
            PLANETS,
        )


def run() -> None:
    db_dir = Path(__file__).parents[2] / "db"
    db_dir.mkdir(exist_ok=True)

    logger.info("Dropping database tables with dbmate...")
    subprocess.run(["dbmate", "drop"], check=True)

    logger.info("Running migrations with dbmate...")
    subprocess.run(["dbmate", "up"], check=True)

    db_client = DBClient(DB_PATH)
    logger.info(f"Seeding test database at {DB_PATH} ...")
    seed_test_db(db_client)
    db_client.close()


if __name__ == "__main__":
    setup_logging()
    run()
