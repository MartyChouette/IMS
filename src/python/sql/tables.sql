-- Users table
CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,  -- in a real application, store a hashed password
    email TEXT NOT NULL UNIQUE
);

-- Products table
CREATE TABLE IF NOT EXISTS products (
    productID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
);

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    orderID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    orderDate DATETIME NOT NULL,
    totalAmount REAL NOT NULL,
    FOREIGN KEY (userID) REFERENCES users(userID)
);

-- OrderItems table
CREATE TABLE IF NOT EXISTS order_items (
    orderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    orderID INTEGER NOT NULL,
    productID INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (orderID) REFERENCES orders(orderID),
    FOREIGN KEY (productID) REFERENCES products(productID)
);

-- Creating an index on the orderDate column
CREATE INDEX idx_order_date ON orders(orderDate);
