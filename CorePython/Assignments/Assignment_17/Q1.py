class Student:

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Accept Method
    def Accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    # Display Method
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

    # Override __str__ Method
    def __str__(self):
        return (f"Student ID : {self.studentId}\n"
                f"Name       : {self.name}\n"
                f"Age        : {self.age}\n"
                f"Percentage : {self.percentage}\n"
                f"Rank       : {self.CalculateRank()}")


# Creating object using parameterized constructor
s1 = Student(101, "Hanmant", 23, 85.5)

# Display
s1.Display()
print()
print("Rank :", s1.CalculateRank())
print()
print("Using __str__:")
print(s1)