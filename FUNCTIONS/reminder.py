import sqlite3

from FUNCTIONS.utils import clear, pause

from logger import setup_logger
logger = setup_logger(name=__name__)


def reminder(cur: sqlite3.Cursor) -> None:
    """Display customers with outstanding balances."""

    clear()
    print("[OUTSTANDING BALANCES]")

    _ = cur.execute("""
        SELECT name, balance
        FROM Customer
        WHERE balance > 0
    """)
    debits: list[tuple[str, float]] = cur.fetchall()

    if debits:
        logger.info(f"Found {len(debits)} customers with outstanding balances")

        for name, debit in debits:
            print(f"- {name}: {debit} €")
            print(f"  -> Hello {name}: You have an outstanding balance of {debit} € to pay.")

    else:
        logger.info("No customers with outstanding balances")
        print("No customers with outstanding balances.")

    pause()
