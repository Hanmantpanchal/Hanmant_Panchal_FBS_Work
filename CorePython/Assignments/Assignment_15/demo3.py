class Shirt:

    # Constructor (Supports parameterized and parameterless)
    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size


    # Destructor
    def __del__(self):
        print("Shirt Object Destroyed")


    # Getter Methods
    def getSid(self):
        return self.sid

    def getSname(self):
        return self.sname

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getSize(self):
        return self.size


    # Setter Methods
    def setSid(self, sid):
        self.sid = sid

    def setSname(self, sname):
        self.sname = sname

    def setType(self, type):
        self.type = type

    def setPrice(self, price):
        self.price = price

    def setSize(self, size):
        self.size = size


    # Show Shirt Details
    def ShowShirt(self):
        print("Shirt ID :", self.getSid())
        print("Shirt Name :", self.getSname())
        print("Type :", self.getType())
        print("Price :", self.getPrice())
        print("Size :", self.getSize())



# Parameterized Constructor
s1 = Shirt(101, "Formal Shirt", "Formal", 1200, "Large")


# Parameterless Constructor
s2 = Shirt()


# Setting values using Setter
s2.setSid(102)
s2.setSname("Casual Shirt")
s2.setType("Casual")
s2.setPrice(900)
s2.setSize("Medium")

print()
print("Shirt 1 Details")
s1.ShowShirt()


print()
print("Shirt 2 Details")
s2.ShowShirt()

print()
print("Getter Example")
print("Shirt Name :", s1.getSname())
print("Size :", s1.getSize())