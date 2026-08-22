# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:

    discount = 10      # Static Variable (10%)

    # Constructor (Parameterized + Parameterless)
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Destructor
    def __del__(self):
        print(f"Product '{self.pname}' object destroyed.")

    # Display Method
    def ShowProduct(self):
        print("Product ID :", self.pid)
        print("Product Name :", self.pname)
        print("Price :", self.price)
        print("Quantity :", self.quantity)

    # Apply Discount
    def applyDiscount(self):
        discountAmount = (self.price * Product.discount) / 100
        finalPrice = self.price - discountAmount
        print("Discount :", Product.discount, "%")
        print("Price After Discount :", finalPrice)


# -------- Main Program --------

# Parameterized Constructor
p1 = Product(101, "Laptop", 50000, 2)

# Parameterless Constructor
p2 = Product()

print("Product 1 Details")
p1.ShowProduct()
p1.applyDiscount()

print("\nProduct 2 Details")
p2.ShowProduct()
p2.applyDiscount()