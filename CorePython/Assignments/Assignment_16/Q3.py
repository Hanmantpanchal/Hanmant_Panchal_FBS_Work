#3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    increment = 10      # Static Variable (10% increase)

    # Constructor (Parameterized + Parameterless)
    def __init__(self, sid=0, sname="", stype="", price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print(f"Shirt '{self.sname}' object destroyed.")

    # Display Method
    def ShowShirt(self):
        print("Shirt ID :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type :", self.stype)
        print("Base Price :", self.price)
        print("Size :", self.size)

    # Calculate Price According to Size
    def calculatePrice(self):
        if self.size.lower() == "small":
            finalPrice = self.price
        elif self.size.lower() == "medium":
            finalPrice = self.price + (self.price * Shirt.increment / 100)
        elif self.size.lower() == "large":
            finalPrice = self.price + (self.price * 2 * Shirt.increment / 100)
        elif self.size.lower() == "xlarge":
            finalPrice = self.price + (self.price * 3 * Shirt.increment / 100)
        else:
            finalPrice = self.price

        print("Final Price :", finalPrice)


# -------- Main Program --------

# Parameterized Constructor
shirt1 = Shirt(101, "Cotton Shirt", "Formal", 1000, "large")

# Parameterless Constructor
shirt2 = Shirt()

print("Shirt 1 Details")
shirt1.ShowShirt()
shirt1.calculatePrice()

print("\nShirt 2 Details")
shirt2.ShowShirt()
shirt2.calculatePrice()