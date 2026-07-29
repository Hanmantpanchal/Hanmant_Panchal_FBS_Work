# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:

    # Constructor (supports parameterized and parameterless)
    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    # Destructor
    def __del__(self):
        print("Book Object Destroyed")

    # Getter Methods
    def getBid(self):
        return self.bid

    def getBname(self):
        return self.bname

    def getPrice(self):
        return self.price

    def getAuthor(self):
        return self.author

    # Setter Methods
    def setBid(self, bid):
        self.bid = bid

    def setBname(self, bname):
        self.bname = bname

    def setPrice(self, price):
        self.price = price

    def setAuthor(self, author):
        self.author = author

    # Show Book Details
    def ShowBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)


# Parameterized Constructor
b1 = Book(101, "Python Programming", 650, "Guido van Rossum")

# Parameterless Constructor
b2 = Book()

# Set values using Setter
b2.setBid(102)
b2.setBname("Java Programming")
b2.setPrice(700)
b2.setAuthor("James Gosling")

print()
print("Book 1 Details")
b1.ShowBook()

print()
print("Book 2 Details")
b2.ShowBook()

print()

print("Getter Example")
print("Book Name :", b1.getBname())
print("Price :", b1.getPrice())