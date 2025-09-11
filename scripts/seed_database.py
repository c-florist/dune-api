from contextlib import closing
from logging import getLogger
from pathlib import Path

from app.core.csv import load_from_csv
from app.core.database import DBClient, run_migrations
from app.core.logging import setup_logging

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "dune.sqlite3"
DATA_DIR = BASE_DIR / "data"

logger = getLogger(__name__)


def seed_data(db_client: DBClient) -> None:
    """Seeds the database with data from CSV files."""
    logger.info("Seeding data...")
    with closing(db_client.conn.cursor()) as cursor:
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
            "INSERT INTO planet (id, uuid, name, geographical_features, ruler) VALUES (?, ?, ?, ?, ?)",
            [(p[0], p[1], p[2], p[3], p[4]) for p in planets],
        )
        logger.info(f"Seeded {len(planets)} planets.")


def main() -> None:
    setup_logging()
    logger.info(f"Database will be created at: {DB_PATH}")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db_client = DBClient(str(DB_PATH), mode="rwc")

    with db_client.conn:
        logger.info("Dropping all existing tables...")
        db_client.conn.executescript(
            """
            DROP VIEW IF EXISTS character_with_org;
            DROP TABLE IF EXISTS character_organisation;
            DROP TABLE IF EXISTS character;
            DROP TABLE IF EXISTS house;
            DROP TABLE IF EXISTS organisation;
            DROP TABLE IF EXISTS planet;
            """
        )

        run_migrations(db_client)
        seed_data(db_client)

    db_client.close()
    logger.info("Database setup and seeding complete.")


if __name__ == "__main__":
    main()
