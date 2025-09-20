from sqlite3 import Cursor
from FUNCTIONS.utils import clear, pause, show_available_customers, sinput

from logger import setup_logger
logger = setup_logger(name=__name__)


def analyse(cur: Cursor) -> None:
    """
    Analyse sales data:
    - Show the total revenue across all purchases.
    - Show the total amount spent and the number of products purchased by a specific customer.
    """
    clear()
    print("[ANALYSE]")

    _ = cur.execute("""
        SELECT SUM(p.price)
        FROM Purchase AS a
        JOIN Product AS p
          ON a.product_id = p.product_id
    """)
    revenue_row = cur.fetchone()  # pyright: ignore[reportAny]
    total_revenue: float = float(revenue_row[0]) if revenue_row and revenue_row[0] is not None else 0.0  # pyright: ignore[reportAny]
    print(f"Total revenue: {total_revenue:.2f} €")


    customers: dict[int, str] = show_available_customers(cur=cur)
    if customers:

        customer_id: int = sinput(txt="Enter customer id: ",choices=set[int](customers.keys()))
        logger.info(msg=f"Selected customer '{customers[customer_id]}', fetching purchases...")

        _ = cur.execute("""
            SELECT SUM(p.price), COUNT(*)
            FROM Purchase AS a
            JOIN Customer AS c
            ON a.customer_id = c.customer_id
            JOIN Product AS p
            ON a.product_id = p.product_id
            WHERE c.customer_id = ?
        """, (customer_id,))
        result = cur.fetchone()  # pyright: ignore[reportAny]

        if result and result[0] is not None:
            total_spent, count = result  # pyright: ignore[reportAny]
            total_spent: float = float(total_spent or 0.0)
            logger.info(msg=f"Customer '{customer_id}': total {total_spent:.2f} €, {count} products")
            print(f"Customer '{customer_id}' has purchased {count} products for {total_spent:.2f} €")
        else:
            logger.warning(msg=f"Customer '{customer_id}' has no purchases")
            print(f"Customer '{customer_id}' has no purchases.")

    else:
        print("No customers")
    pause()
