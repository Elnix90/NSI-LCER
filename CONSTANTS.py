from pathlib import Path
import logging



DB: Path =Path( "db.db")

LOGS_DIR: Path = Path("LOGS")

LOGS_CONSOLE_GLOBALLY: bool = True
LOGGING_LEVEL_CONSOLE: int = logging.WARNING
LOGGING_LEVEL_LOGFILES: int = logging.DEBUG
NOT_OVERLAP_FPRINT: bool = False


MENU = """
Welcome to LCER

  0 : Exit the menu and quit the program
Manager menu:
  1 : Reminder for outstanding payment
  2 : Sales analysis
  3 : Shipment of a purchase
Customer menu:
  4 : Purchase a product
  5 : Pay outstanding balance
"""
