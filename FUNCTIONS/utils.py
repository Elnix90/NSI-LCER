import os
from sqlite3 import Cursor


from logger import setup_logger
logger = setup_logger(name=__name__)


def get_cons_width() -> int:
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def clear() -> None:
    _ = os.system('clear')


def pause() -> None:
    print("━" * get_cons_width())
    _ = input("Press [Enter] to continue...")
    clear()








def get_customers(cur: Cursor) ->  dict[int, str]:
    _ = cur.execute("""
        SELECT customer_id, name
        FROM Customer
    """)
    customers_raw: list[tuple[int, str]] = cur.fetchall()
    customers: dict[int, str] = {id: name for id, name in customers_raw}
    logger.info(msg=f"[Get customers] Found {len(customers)} customers")
    return customers

def show_available_customers(cur: Cursor) -> dict[int, str]:
    customers: dict[int, str] = get_customers(cur=cur)
    if customers:
        print(f"{len(customers)} customers:")
        for id, customer in customers.items():
            print(f"- {id} : {customer}")
    return customers







def get_procucts(cur: Cursor) ->  dict[int, str]:
    _ = cur.execute("""
        SELECT product_id, name
        FROM Product
    """)
    products_raw: list[tuple[int, str]] = cur.fetchall()
    products: dict[int, str] = {id: name for id, name in products_raw}
    logger.info(msg=f"[Get products] Found {len(products)} products")
    return products

def show_available_products(cur: Cursor) -> dict[int, str]:
    products: dict[int, str] = get_procucts(cur=cur)
    if products:
        print(f"{len(products)} products:")
        for id, product in products.items():
            print(f"- {id} : {product}")
    return products







def sinput(txt: str, choices: set[int]) -> int:
    while True:
        choice = input(txt)
        try:
            choice_int: int = int(choice)
            if choice_int not in choices:
                print(f"Choice '{choice}' is not allowed, try again")
            else:
                return choice_int
        except Exception:
            continue