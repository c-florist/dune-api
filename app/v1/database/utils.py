from pathlib import Path

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


def run_migrations() -> None:
    ...
