import sqlite3
from pathlib import Path
from CONSTANTS import DB
from logger import setup_logger

logger = setup_logger(__name__)


def get_db_connection(sql_file: str = "create_db.sql") -> sqlite3.Connection:
    """
    Connect to the SQLite database. If it does not exist or is broken, create it using the provided SQL script.
    """

    sql_path = Path(sql_file)

    try:
        if DB.exists():
            # Try connecting normally
            conn = sqlite3.connect(DB)
            conn.row_factory = sqlite3.Row
            logger.debug("[Get DB conn] Successfully connected")
            return conn
        else: raise sqlite3.Error(f"DB file does not exists: {DB}")

    except sqlite3.Error as e:
        logger.warning(f"Database connection failed: {e}")
        logger.info("Attempting to create the database from SQL script...")

        if not sql_path.exists():
            logger.error(f"SQL file not found: {sql_path}")
            raise FileNotFoundError(f"SQL file not found: {sql_path}")

        # Create the database from SQL script
        try:
            conn = sqlite3.connect(DB)
            conn.row_factory = sqlite3.Row
            with sql_path.open("r", encoding="utf-8") as f:
                sql_script = f.read()
            _ = conn.executescript(sql_script)
            conn.commit()
            logger.info(f"Database created successfully from {sql_file}")
            return conn
        except sqlite3.Error as e2:
            logger.exception(f"Failed to create database: {e2}")
            raise
