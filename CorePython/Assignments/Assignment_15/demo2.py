class Product:

    # Constructor (Supports parameterized and parameterless)
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity


    # Destructor
    def __del__(self):
        print("Product Object Destroyed")


    # Getter Methods
    def getPid(self):
        return self.pid

    def getPname(self):
        return self.pname

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity


    # Setter Methods
    def setPid(self, pid):
        self.pid = pid

    def setPname(self, pname):
        self.pname = pname

    def setPrice(self, price):
        self.price = price

    def setQuantity(self, quantity):
        self.quantity = quantity


    # Show Product Details
    def ShowProduct(self):
        print("Product ID :", self.getPid())
        print("Product Name :", self.getPname())
        print("Price :", self.getPrice())
        print("Quantity :", self.getQuantity())
        print("Total Amount :", self.price * self.quantity)



# Parameterized Constructor
p1 = Product(101, "Laptop", 50000, 2)

# Parameterless Constructor
p2 = Product()


# Setting values using Setter
p2.setPid(102)
p2.setPname("Mobile")
p2.setPrice(20000)
p2.setQuantity(3)

print()
print("Product 1 Details")
p1.ShowProduct()

print()
print("Product 2 Details")
p2.ShowProduct()

print()
print("Getter Example")
print("Product Name :", p1.getPname())
print("Price :", p1.getPrice())