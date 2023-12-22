import product
import sqlite3
import os

print("Current working directory:", os.getcwd())

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the SQL and database files
sql_file_path = os.path.join(current_dir, 'sql/tables.sql')
db_file_path = os.path.join(current_dir, 'sql/database.db')

# Ensure the 'sql' directory exists
sql_directory = os.path.join(current_dir, 'sql')
if not os.path.exists(sql_directory):
    os.makedirs(sql_directory)

# Initialize database
def init_db():
    with sqlite3.connect(db_file_path) as conn:
        with open(sql_file_path, 'r') as f:
            conn.executescript(f.read())

if __name__ == "__main__":
    init_db()

    # Establish a connection and create a cursor
    connection = sqlite3.connect(db_file_path)
    cursor = connection.cursor()

    # Add a new product
    new_product = product.AddProduct(None, "Apple", 0.50, 100)  # productID is set to None

    # Insert the product into the database
    insert_command = "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)"
    cursor.execute(insert_command, (new_product.name, new_product.price, new_product.qty))

    # Retrieve and print all products
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)

    # Assuming you want to update the first product added
    productID_to_update = cursor.lastrowid
    updated_product = product.UpdateProduct(productID_to_update, "Green Apple", 0.55, 120)

    # Update the product's details
    update_command = "UPDATE products SET name = ?, price = ?, quantity = ? WHERE productID = ?"
    cursor.execute(update_command, (updated_product.name, updated_product.price, updated_product.qty, updated_product.productID))
    connection.commit()

    # Retrieve and print the updated product
    cursor.execute("SELECT * FROM products WHERE productID = ?", (updated_product.productID,))
    print(cursor.fetchone())

    # Close the connection
    cursor.close()
    connection.close()
