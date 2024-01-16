from logging import getLogger
from glob import glob
from pathlib import Path

from .client import DbClient

logger = getLogger(__name__)
MIGRATIONS_DIR = Path(__file__).parent / "migrations"


def run_migrations(db_client: DbClient) -> None:
    migrations = [Path(x) for x in glob(f"{MIGRATIONS_DIR}/*.sql")]
    logger.info(f"Found {len(migrations)} migrations in {MIGRATIONS_DIR} ...")

    with db_client.conn as conn:
        for file in migrations:
            logger.info(f"Running migration: {file.name} ...")
            sql = file.read_text()
            conn.executescript(sql)

    logger.info(f"Successfully executed all migrations")
