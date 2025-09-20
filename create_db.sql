CREATE TABLE IF NOT EXISTS Product (
    product_id INTEGER PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    price REAL NOT NULL,
    stock INT NOT NULL,
    CHECK (0 < price AND price < 2000),
    CHECK (0 <= stock AND stock < 10000)
);

CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    age INT,
    address VARCHAR(20) NOT NULL,
    balance REAL NOT NULL,
    CHECK (0 < age AND age <= 130),
    CHECK (0 <= balance AND balance < 2000)
);

CREATE TABLE IF NOT EXISTS Purchase (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    shipped BOOLEAN NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

INSERT OR IGNORE INTO Product VALUES (99, 'teddy', 5, 1000);
INSERT OR IGNORE INTO Product VALUES (95, 'blouse', 20, 500);
INSERT OR IGNORE INTO Product VALUES (92, 'tie', 15, 9900);
INSERT OR IGNORE INTO Product VALUES (97, 'porsche', 1000, 12);

INSERT OR IGNORE INTO Customer VALUES (27, 'Rita', 17, 'Rio', 20);
INSERT OR IGNORE INTO Customer VALUES (29, 'Riton', 18, 'Cayeux', 0);
INSERT OR IGNORE INTO Customer VALUES (23, 'Jeanne', 19, 'New York', 300);

INSERT OR IGNORE INTO Purchase VALUES (1, 99, 29, 1);
INSERT OR IGNORE INTO Purchase VALUES (2, 95, 27, 0);
INSERT OR IGNORE INTO Purchase VALUES (3, 99, 23, 0);
INSERT OR IGNORE INTO Purchase VALUES (4, 97, 27, 1);
