import product
import sqlite3

# Establish a connection and create a cursor
connection = sqlite3.connect('test_database.db')
cursor = connection.cursor()

# SQL command to create the table
create_table_command = """
CREATE TABLE IF NOT EXISTS products (
    productID INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    quantity INTEGER
);
"""

# Execute the command
cursor.execute(create_table_command)

# Commit the changes
connection.commit()


new_product = product.AddProduct(101, "Apple", 0.50, 100)

#print(f"New Product: ID={new_product.productID}, Name={new_product.name}, Price={new_product.price}, Quantity={new_product.qty}")

# Insert the product into the database
insert_command = "INSERT INTO products (productID, name, price, quantity) VALUES (?, ?, ?, ?)"
cursor.execute(insert_command, (new_product.productID, new_product.name, new_product.price, new_product.qty))

# Retrieve and print all products
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)


# Update the product's details
updated_product = product.UpdateProduct(new_product.productID, "Green Apple", 0.55, 120)
update_command = "UPDATE products SET name = ?, price = ?, quantity = ? WHERE productID = ?"
cursor.execute(update_command, (updated_product.name, updated_product.price, updated_product.qty, updated_product.productID))
connection.commit()

# Retrieve and print the updated product
cursor.execute("SELECT * FROM products WHERE productID = ?", (updated_product.productID,))
print(cursor.fetchone())

# Close the connection
cursor.close()
connection.close()