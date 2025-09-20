from sqlite3 import Connection, Cursor

from FUNCTIONS.utils import clear, get_cons_width
from CONSTANTS import MENU
from FUNCTIONS.purchase import purchase
from FUNCTIONS.analyse import analyse
from FUNCTIONS.expedition import expedition
from FUNCTIONS.payment import payment
from FUNCTIONS.reminder import reminder
from sql import get_db_connection

from logger import setup_logger
logger = setup_logger(name=__name__)


def menu(cur: Cursor, conn: Connection) -> None:
    """Display the main menu and route user choices to the correct function."""

    while True:
        clear()
        print("█" * get_cons_width())
        print(MENU)
        print("█" * get_cons_width())

        try:
            n: int = int(input("Select an action: "))
            logger.info(f"User choice: {n}")
        except ValueError:
            logger.warning("Invalid input: not an integer")
            continue

        match n:
            case 0:
                logger.info("Program exited by user")
                return
            case 1:
                reminder(cur=cur)
            case 2:
                analyse(cur=cur)
            case 3:
                expedition(cur=cur, conn=conn)
            case 4:
                purchase(cur=cur, conn=conn)
            case 5:
                payment(cur=cur, conn=conn)
            case _:
                logger.warning(f"Unavailable choice: {n}")
                print("Choice unavailable.")


def main() -> None:
    """Entry point: set up database connection and start the menu."""
    with get_db_connection() as conn:
        cur: Cursor = conn.cursor()
        menu(cur=cur, conn=conn)


if __name__ == "__main__":
    main()
