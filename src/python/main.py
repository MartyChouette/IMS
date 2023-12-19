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

# Close the connection
cursor.close()
connection.close()


# Updating the product's name
updated_product = product.UpdateProduct(new_product.productID, new_product.name, new_product.price, new_product.qty)

# Now update the name
updated_product.update_name("Green Apple")

# Print updated product details
#print(f"Updated Product: ID={updated_product.productID}, Name={updated_product.name}, Price={updated_product.price}, Quantity={updated_product.qty}")
