import logging
import os
from CONSTANTS import LOGS_DIR, LOGGING_LEVEL_LOGFILES


def setup_logger(name: str) -> logging.Logger:
    """
    Set up a logger that writes logs to a file in LOGS_DIR.
    Console output is disabled.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        os.makedirs(LOGS_DIR, exist_ok=True)

        # File formatter (plain, no colors)
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # File handler
        log_path = os.path.join(LOGS_DIR, f"{name}.log")
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel(LOGGING_LEVEL_LOGFILES)
        fh.setFormatter(file_formatter)
        logger.addHandler(fh)

    return logger
