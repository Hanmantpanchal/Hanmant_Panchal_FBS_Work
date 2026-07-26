# Base Class
class Book:

    def __init__(self, title, author, edition):
        self.title = title
        self.author = author
        self.edition = edition

    # Getter and Setter for Title
    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    # Getter and Setter for Author
    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    # Getter and Setter for Edition
    def getEdition(self):
        return self.edition

    def setEdition(self, edition):
        self.edition = edition

    # Display Method
    def display(self):
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Edition :", self.edition)


# Derived Class : StoryBook
class StoryBook(Book):

    def __init__(self, title, author, edition, genre):
        super().__init__(title, author, edition)
        self.genre = genre

    # Getter and Setter for Genre
    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    # Display Method
    def display(self):
        super().display()
        print("Genre   :", self.genre)


# Derived Class : SubjectBook
class SubjectBook(Book):

    def __init__(self, title, author, edition, subject):
        super().__init__(title, author, edition)
        self.subject = subject

    # Getter and Setter for Subject
    def getSubject(self):
        return self.subject

    def setSubject(self, subject):
        self.subject = subject

    # Display Method
    def display(self):
        super().display()
        print("Subject :", self.subject)



story1 = StoryBook("Harry Potter", "J.K. Rowling", "5th", "Fantasy")
subject1 = SubjectBook("Python Programming", "Guido van Rossum", "3rd", "Python")



print("Story Book Details")
print("Title :", story1.getTitle())
print("Author :", story1.getAuthor())
print("Edition :", story1.getEdition())
print("Genre :", story1.getGenre())

print()

print("Subject Book Details")
print("Title :", subject1.getTitle())
print("Author :", subject1.getAuthor())
print("Edition :", subject1.getEdition())
print("Subject :", subject1.getSubject())