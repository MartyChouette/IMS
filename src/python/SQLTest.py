import sqlite3
import unittest

class SQLTest(unittest.TestCase):
    def setUp(self):
        # Connect to an in-memory SQLite database for testing
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        # Create a test table
        self.cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")

        # Insert test data
        self.cursor.execute("INSERT INTO products (name, price) VALUES ('Apple', 0.50)")
        self.cursor.execute("INSERT INTO products (name, price) VALUES ('Banana', 0.30)")

    def test_product_count(self):
        # Test the count of products
        self.cursor.execute("SELECT COUNT(*) FROM products")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_product_insert(self):
        # Test insertion of a product
        self.cursor.execute("INSERT INTO products (name, price) VALUES ('Orange', 0.40)")
        self.cursor.execute("SELECT COUNT(*) FROM products")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 3)

    def tearDown(self):
        self.connection.close()

if __name__ == '__main__':
    unittest.main()
