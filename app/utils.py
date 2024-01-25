import logging
from glob import glob
from logging import getLogger
from pathlib import Path

from .constants import ENV
from .v1.database import DbClient

MIGRATIONS_DIR = Path(__file__).parent / "migrations"
logger = getLogger(__name__)


def setup_logging() -> None:
    if ENV != "local":
        logging_level = logging.INFO
    else:
        logging_level = logging.DEBUG

    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s %(levelname)s:%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def run_migrations(db_client: DbClient) -> None:
    migrations = [Path(x) for x in glob(f"{MIGRATIONS_DIR}/*.sql")]
    logger.info(f"Found {len(migrations)} migrations in {MIGRATIONS_DIR} ...")

    with db_client.conn as conn:
        for file in migrations:
            logger.info(f"Running migration: {file.name} ...")
            sql = file.read_text()
            conn.executescript(sql)

    logger.info(f"Successfully executed all migrations")
