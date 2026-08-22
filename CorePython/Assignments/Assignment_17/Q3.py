# 3. Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
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
class MedicalStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage,
                 specialization, marksOfInternship):

        # Calling Parent Constructor
        super().__init__(studentId, name, age, percentage)

        # Child class data members
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    # Override Accept
    def Accept(self):

        # Accept parent class data
        super().Accept()

        # Accept child class data
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(
            input("Enter Marks of Internship: ")
        )

    # Override Display
    def Display(self):

        # Display parent class data
        super().Display()

        # Display child class data
        print("Specialization      :", self.specialization)
        print("Marks of Internship :", self.marksOfInternship)

    # Override CalculateRank
    def CalculateRank(self):

        if self.percentage >= 75 and self.marksOfInternship >= 40:
            return "Distinction"

        elif self.percentage >= 60 and self.marksOfInternship >= 35:
            return "First Class"

        elif self.percentage >= 50 and self.marksOfInternship >= 30:
            return "Second Class"

        elif self.percentage >= 35 and self.marksOfInternship >= 25:
            return "Pass Class"

        else:
            return "Fail"

    # Override __str__
    def __str__(self):

        return (f"Student ID          : {self.studentId}\n"
                f"Name                : {self.name}\n"
                f"Age                 : {self.age}\n"
                f"Percentage          : {self.percentage}\n"
                f"Specialization      : {self.specialization}\n"
                f"Marks of Internship : {self.marksOfInternship}\n"
                f"Rank                : {self.CalculateRank()}")


# Create MedicalStudent object
m1 = MedicalStudent(
    201,
    "Rahul",
    23,
    82.5,
    "Cardiology",
    45
)

# Display
m1.Display()

# Calculate Rank
print("\nRank :", m1.CalculateRank())

# __str__
print("\nUsing __str__:")
print(m1)