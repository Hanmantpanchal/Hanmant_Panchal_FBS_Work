from SYMARKS import SYMARKS
from tymarks import TYMarks


class Student:

    def __init__(self, rollNo, name, syMarks, tyMarks):
        self.rollNo = rollNo
        self.name = name
        self.syMarks = syMarks
        self.tyMarks = tyMarks

    # Getter
    def getRollNo(self):
        return self.rollNo

    # Setter
    def setRollNo(self, rollNo):
        self.rollNo = rollNo

    # Getter
    def getName(self):
        return self.name

    # Setter
    def setName(self, name):
        self.name = name

    # Getter
    def getSYMarks(self):
        return self.syMarks

    # Setter
    def setSYMarks(self, syMarks):
        self.syMarks = syMarks

    # Getter
    def getTYMarks(self):
        return self.tyMarks

    # Setter
    def setTYMarks(self, tyMarks):
        self.tyMarks = tyMarks

    def calculateResult(self):

        syComputer = self.syMarks.getComputerTotal()

        tyComputer = (
            self.tyMarks.getTheory()
            + self.tyMarks.getPractical()
        )

        percentage = (syComputer + tyComputer) / 2

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return percentage, grade

    def display(self):

        percentage, grade = self.calculateResult()

        print("\n------------- Student Result -------------")

        print("Roll No      :", self.getRollNo())
        print("Name         :", self.getName())
        print("SY Computer  :", self.syMarks.getComputerTotal())
        print("TY Theory    :", self.tyMarks.getTheory())
        print("TY Practical :", self.tyMarks.getPractical())
        print("Percentage   :", percentage)
        print("Grade        :", grade)

        print("------------------------------------------")


# Create SYMARKS object
sy = SYMARKS(75, 80, 70)

# Create TYMarks object
ty = TYMarks(40, 30)

# Create Student object
s1 = Student(101, "Hanmant", sy, ty)

# Display
s1.display()

# Update marks
print("\nAfter Updating Marks:")

sy.setComputerTotal(85)
ty.setTheory(45)
ty.setPractical(35)

s1.display()

# Update student name
s1.setName("Rahul")

print("\nAfter Updating Student Name:")
print("Name:", s1.getName())