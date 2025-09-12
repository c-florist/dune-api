from contextlib import closing
from logging import getLogger
from pathlib import Path

from app.core.constants import DB_PATH
from app.core.csv import load_from_csv
from app.core.database import DBClient
from app.core.logging import setup_logging

BASE_DIR = Path(__file__).parents[1]
DATA_DIR = BASE_DIR / "data"

logger = getLogger(__name__)


def seed_data(db_client: DBClient) -> None:
    logger.info("Seeding data...")
    with closing(db_client.conn.cursor()) as cursor:
        # Only delete from system data tables
        cursor.executescript(
            """
            DELETE FROM character_organisation;
            DELETE FROM character;
            DELETE FROM house;
            DELETE FROM organisation;
            DELETE FROM planet;
            """
        )

        houses = load_from_csv(DATA_DIR / "house.csv")
        cursor.executemany(
            "INSERT INTO house (id, uuid, name, homeworld, status, colours, symbol) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(h[0], h[1], h[2], h[3], h[4], h[5], h[6]) for h in houses],
        )
        logger.info(f"Seeded {len(houses)} houses.")

        organisations = load_from_csv(DATA_DIR / "organisation.csv")
        cursor.executemany(
            "INSERT INTO organisation (id, uuid, name, founded, dissolved, misc) VALUES (?, ?, ?, ?, ?, ?)",
            [(o[0], o[1], o[2], o[3], o[4], o[5]) for o in organisations],
        )
        logger.info(f"Seeded {len(organisations)} organisations.")

        characters = load_from_csv(DATA_DIR / "character.csv")
        cursor.executemany(
            """
                INSERT INTO character (
                    id,
                    uuid,
                    titles,
                    aliases,
                    first_name,
                    last_name,
                    suffix,
                    dob,
                    birthplace,
                    dod,
                    profession,
                    misc,
                    house_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12]) for c in characters],
        )
        logger.info(f"Seeded {len(characters)} characters.")

        character_orgs = load_from_csv(DATA_DIR / "character_organisation.csv")
        cursor.executemany(
            "INSERT INTO character_organisation (character_id, org_id) VALUES (?, ?)",
            character_orgs,
        )
        logger.info(f"Seeded {len(character_orgs)} character-organisation relationships.")

        planets = load_from_csv(DATA_DIR / "planet.csv")
        cursor.executemany(
            "INSERT INTO planet (id, uuid, name, environment, ruler) VALUES (?, ?, ?, ?, ?)",
            [(p[0], p[1], p[2], p[3], p[4]) for p in planets],
        )
        logger.info(f"Seeded {len(planets)} planets.")


def main() -> None:
    setup_logging()
    logger.info(f"Connecting to database at: {DB_PATH}")
    db_client = DBClient(str(DB_PATH), mode="rwc")

    seed_data(db_client)

    db_client.close()
    logger.info("Database seeding complete.")


if __name__ == "__main__":
    main()
