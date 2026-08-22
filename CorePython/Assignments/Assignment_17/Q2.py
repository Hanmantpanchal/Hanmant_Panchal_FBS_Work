# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method


class Student:

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Accept
    def Accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    # Display
    def Display(self):
        print("Student ID :", self.studentId)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Percentage :", self.percentage)

    # Calculate Rank
    def CalculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 35:
            return "Pass Class"
        else:
            return "Fail"

    # __str__
    def __str__(self):
        return (f"Student ID : {self.studentId}\n"
                f"Name       : {self.name}\n"
                f"Age        : {self.age}\n"
                f"Percentage : {self.percentage}\n"
                f"Rank       : {self.CalculateRank()}")


# Derived Class
class EnggStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage,
                 branch, internalMarks):

        # Calling Parent Constructor
        super().__init__(studentId, name, age, percentage)

        self.branch = branch
        self.internalMarks = internalMarks

    # Override Accept
    def Accept(self):
        super().Accept()

        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    # Override Display
    def Display(self):
        super().Display()
        print("Branch       :", self.branch)
        print("Internal Marks:", self.internalMarks)

    # Override CalculateRank
    def CalculateRank(self):

        if self.percentage >= 75 and self.internalMarks >= 40:
            return "Distinction"

        elif self.percentage >= 60 and self.internalMarks >= 35:
            return "First Class"

        elif self.percentage >= 50 and self.internalMarks >= 30:
            return "Second Class"

        elif self.percentage >= 35 and self.internalMarks >= 25:
            return "Pass Class"

        else:
            return "Fail"

    # Override __str__
    def __str__(self):
        return (f"Student ID     : {self.studentId}\n"
                f"Name           : {self.name}\n"
                f"Age            : {self.age}\n"
                f"Percentage     : {self.percentage}\n"
                f"Branch         : {self.branch}\n"
                f"Internal Marks : {self.internalMarks}\n"
                f"Rank           : {self.CalculateRank()}")


# Create EnggStudent object
e1 = EnggStudent(
    101,
    "Hanmant",
    23,
    82.5,
    "Computer Engineering",
    45
)

# Display
e1.Display()

print("\nRank :", e1.CalculateRank())

print("\nUsing __str__:")
print(e1)