  # Multiple Inheritance

class Sports:

    def __init__(self, sport):
        self.sport = sport

    def displaySports(self):
        print(f"Sport : {self.sport}")


class Student:

    def __init__(self, rollNo):
        self.rollNo = rollNo

    def displayStudent(self):
        print(f"Roll No : {self.rollNo}")


class Player(Sports, Student):

    def __init__(self, sport, rollNo, name):
        Sports.__init__(self, sport)
        Student.__init__(self, rollNo)
        self.name = name

    def display(self):
        self.displaySports()
        self.displayStudent()
        print(f"Name : {self.name}")


p1 = Player("Cricket", 101, "Hanmant")
p1.display()