import logging

from .constants import ENV


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
