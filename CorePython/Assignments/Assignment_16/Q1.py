# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:

    count = 0          # Static Variable

    # Constructor (Parameterized + Parameterless)
    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count += 1      # Increase object count

    # Destructor
    def __del__(self):
        print(f"Book '{self.bname}' object destroyed.")

    # Display Method
    def ShowBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)

    # Static Method to Display Count
    @staticmethod
    def showCount():
        print("Total Objects Created :", Book.count)


# -------- Main Program --------

# Parameterized Constructor
book1 = Book(101, "Python", 500, "Guido")

# Parameterless Constructor
book2 = Book()

print("Book 1 Details")
book1.ShowBook()

print("\nBook 2 Details")
book2.ShowBook()

print()
Book.showCount()