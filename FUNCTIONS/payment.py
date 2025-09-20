from sqlite3 import Connection, Cursor

from FUNCTIONS.utils import clear, pause, show_available_customers, sinput

from logger import setup_logger
logger = setup_logger(name=__name__)


def payment(cur: Cursor, conn: Connection) -> None:
    """Handle customer payment to reduce outstanding debit."""

    clear()
    print("[PAYMENT]")

    customers: dict[int, str] = show_available_customers(cur=cur)
    if customers:

        customer_id: int = sinput(txt="Customer id: ", choices=set[int](customers.keys()))
        logger.info(f"Payment for customer ID: {customer_id}")

        _ = cur.execute("""
            SELECT balance
            FROM Customer
            WHERE customer_id = ?
        """,
            (customer_id,)
        )

        result = cur.fetchone()  # pyright: ignore[reportAny]
        if result and result[0] >= 0:

            debit: float = float(result[0])  # pyright: ignore[reportAny]
            if debit > 0:
                print(f"Your current debit is {debit} €")

                try:
                    amount: float = float(input("Payment amount: "))
                    logger.info(f"Payment amount: {amount} €")

                    if amount <= debit:

                        _ = cur.execute("""
                            UPDATE Customer
                            SET balance = balance - ?
                            WHERE customer_id = ?
                        """,
                            (amount, customer_id),
                        )
                        conn.commit()

                        new_debit: float = debit - amount
                        logger.info(msg=f"Payment completed: previous debit {debit} €, new debit {new_debit} €")
                        print(f"New debit: {new_debit} €")

                    else:
                        logger.warning(f"Payment {amount} exceeds debit {debit}")
                        print(f"Payment {amount} exceeds debit {debit}")

                except ValueError:
                    logger.error("Invalid payment amount")
                    print("Invalid payment amount.")
            else:
                print("Nothing to pay")
        else:
            logger.warning(f"Customer ID {customer_id} has no outstanding debit")
            print(f"Customer ID {customer_id} has no outstanding debit")

    else:
        print("No customer found.")

    pause()
