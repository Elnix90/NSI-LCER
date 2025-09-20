from sqlite3 import Connection, Cursor
from FUNCTIONS.utils import clear, pause, show_available_customers, show_available_products, sinput

from logger import setup_logger
logger = setup_logger(name=__name__)


def purchase(cur: Cursor, conn: Connection) -> None:
    """Handle a product purchase for a customer."""

    clear()
    print("[PURCHASE]")

    customers: dict[int, str] = show_available_customers(cur=cur)
    if customers:

        customer_id: int = sinput(txt="YOUR customer id: ", choices=set[int](customers.keys()))
        logger.info(f"Purchase for customer: {customers[customer_id]} (ID: {customer_id})")

        products: dict[int, str] = show_available_products(cur=cur)
        if products:
            product_id: int = sinput("Product id: ",set[int](products.keys()))
            logger.info(f"Requested product: {products[product_id]} (ID: {product_id})")

            _ = cur.execute("""
                INSERT INTO Purchase (customer_id, product_id, shipped)
                VALUES ( ?, ?, 0)
            """, (customer_id, product_id))

            _ = cur.execute("""
                SELECT price
                FROM Product
                WHERE product_id = ?
            """,(product_id,))
            price = cur.fetchone()[0]  # pyright: ignore[reportAny]

            _ = cur.execute("""
                UPDATE Customer
                SET balance = balance + ?
                WHERE customer_id = ?
            """, (price, customer_id)
            )

            conn.commit()

            logger.info(msg=f"Purchase added; Product: {product_id}, Price: {price} €")
            print("Purchase added")

        else:
            print("No products found")

    else:
        print("No customers found")

    pause()
