import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = "app.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)


def get_logger(name: str) -> logging.Logger:
    """Logger Init and Config"""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler with rotation
        file_handler = RotatingFileHandler(
            LOG_PATH,
            maxBytes=5_000_000,
            backupCount=3
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger