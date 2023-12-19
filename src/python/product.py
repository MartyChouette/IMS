class AddProduct:
    def __init__(self, productID, name, price, qty):
        self.productID = productID
        self.name = name
        self.price = price
        self.qty = qty

class UpdateProduct(AddProduct):
    def __init__(self, productID, name, price, qty):
        super().__init__(productID, name, price, qty)

    def update_name(self, new_name):
        self.name = new_name

    def update_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price cannot be negative.")

    def update_qty(self, new_qty):
        if new_qty >= 0:
            self.qty = new_qty
        else:
            raise ValueError("Quantity cannot be negative.")
