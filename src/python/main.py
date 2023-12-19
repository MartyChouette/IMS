import product
import sqlite3
connection = sqlite3.connect('test_database.db')  # This creates a new file 'test_database.db'
cursor = connection.cursor()
# You can now create tables and insert data


new_product = product.AddProduct(101, "Apple", 0.50, 100)

print(f"New Product: ID={new_product.productID}, Name={new_product.name}, Price={new_product.price}, Quantity={new_product.qty}")

# Updating the product's name
updated_product = product.UpdateProduct(new_product.productID, new_product.name, new_product.price, new_product.qty)

# Now update the name
updated_product.update_name("Green Apple")

# Print updated product details
print(f"Updated Product: ID={updated_product.productID}, Name={updated_product.name}, Price={updated_product.price}, Quantity={updated_product.qty}")
