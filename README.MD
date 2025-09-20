
---

# LCER Project

## Overview

LCER is a Python-based imaginary project of NSI, it is made for learning the usage of sql in python

---

## Features

* **Customer management:** View customers, track balances, and process payments.
* **Product management:** List available products and handle stock updates.
* **Purchases:** Record product purchases for customers and update their outstanding balances.
* **Expedition/Shipping:** Mark purchases as shipped and decrement product stock.
* **Outstanding balance reminders:** List customers with unpaid balances and generate email-style notifications.
* **Sales analysis:** Basic reporting of sales data.
* **Logging:** Detailed logging of all operations to files.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Elnix90/NSI-LCER.git
```

2. Navigate to the project directory:

```bash
cd NSI-LCER
```

3. Ensure Python 3.8+ is installed.
4. The project uses an SQLite database. The first time you run the program, the database will be created automatically using the included `create_db.sql` script.

---

## Usage

Run the main menu:

```bash
python menu.py
```

You will be presented with a menu:

```
Welcome to LCER

  0 : Exit program
Manager Menu:
  1 : Send payment reminders
  2 : Analyze sales
  3 : Ship a purchase
Customer Menu:
  4 : Make a purchase
  5 : Make a payment
```

Follow the prompts to interact with customers, products, and purchases.

---

## Notes

* All logs are saved in the `LOGS` directory.
* Database tables are automatically created if missing, with default sample data for products, customers, and purchases.

---

## Dependencies

* Python 3.8+
* SQLite3 (bundled with Python)

---

## License

This project is open source.

