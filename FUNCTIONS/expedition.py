from sqlite3 import Connection, Cursor
from FUNCTIONS.utils import clear, pause

from logger import setup_logger
logger = setup_logger(name=__name__)


def expedition(cur: Cursor, conn: Connection) -> None:
    """Ship purchases that have not yet been shipped."""

    clear()
    print("[EXPEDITION]")

    _ = cur.execute("""
        SELECT purchase_id, product_id
        FROM Purchase
        WHERE shipped = 0
    """)
    pending: list[tuple[int, int]] = cur.fetchall()

    if pending:

        for purchase_id, product_id in pending:
            print(f"Shipping purchase_id {purchase_id}")
            _ = cur.execute("""
                UPDATE Product
                SET stock = stock - 1
                WHERE product_id = ?
            """,
                (product_id,),
            )

            _ = cur.execute("""
                UPDATE Purchase
                SET shipped = 1
                WHERE purchase_id = ?
            """,
                (purchase_id,),
            )

            conn.commit()
            
            logger.info(f"Purchase {purchase_id} shipped successfully")
            print("Purchase shipped.")

    else:
        logger.info("No purchases to ship")
        print("No purchases to ship.")

    pause()
