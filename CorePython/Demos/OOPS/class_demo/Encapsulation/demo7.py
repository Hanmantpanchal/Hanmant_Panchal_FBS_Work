# Write a class program to set and get book details

class Book:

    # Constructor
    def __init__(self, BookId, Title, Author, Publisher, Edition):
        self.BookId = BookId
        self.Title = Title
        self.Author = Author
        self.Publisher = Publisher
        self.Edition = Edition

    # Getter and Setter for BookId
    def getBookId(self):
        return self.BookId

    def setBookId(self, BookId):
        self.BookId = BookId

    # Getter and Setter for Title
    def getTitle(self):
        return self.Title

    def setTitle(self, Title):
        self.Title = Title

    # Getter and Setter for Author
    def getAuthor(self):
        return self.Author

    def setAuthor(self, Author):
        self.Author = Author

    # Getter and Setter for Publisher
    def getPublisher(self):
        return self.Publisher

    def setPublisher(self, Publisher):
        self.Publisher = Publisher

    # Getter and Setter for Edition
    def getEdition(self):
        return self.Edition

    def setEdition(self, Edition):
        self.Edition = Edition

    # Display Book Details
    def display(self):
        print("Book ID   :", p1.getBookId())
        print("Title     :", p1.getTitle())
        print("Author    :", p1.getAuthor())
        print("Publisher :", p1.getPublisher())
        print("Edition   :", p1.getEdition())




p1 = Book(101, "Python Programming", "Guido van Rossum", "Pearson", "3rd Edition")
p2 = Book(102, "Database Management System", "Korth", "McGraw Hill", "7th Edition")
p3 = Book(103, "Data Structures", "Seymour Lipschutz", "Schaum's Outline", "2nd Edition")




print()

p1.setBookId(201)
p1.setTitle("Advanced Python")
p1.setAuthor("Mark Lutz")
p1.setPublisher("O'Reilly")
p1.setEdition("5th Edition")

print()

p2.display()

print(p2.getTitle())