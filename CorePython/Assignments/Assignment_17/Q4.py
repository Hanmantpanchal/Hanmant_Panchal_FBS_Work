class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return (f"Student ID : {self.studentId}\n"
                f"Name       : {self.name}\n"
                f"Age        : {self.age}\n"
                f"Percentage : {self.percentage}")


class College:

    # Parameterized Constructor
    def __init__(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents
        self.students = []

    # Add Student
    def AddStudent(self, student):

        if len(self.students) < self.numberOfStudents:
            self.students.append(student)
            print("Student added successfully.")
        else:
            print("College is full.")

    # Get Student
    def GetStudent(self, studentId):

        for student in self.students:

            if student.studentId == studentId:
                return student

        return None

    # Remove Student
    def RemoveStudent(self, studentId):

        student = self.GetStudent(studentId)

        if student is not None:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    # __str__
    def __str__(self):

        result = "College Students:\n"

        for student in self.students:
            result += str(student)
            result += "\n----------------------\n"

        return result


# Create students
s1 = Student(101, "Rahul", 21, 85.5)
s2 = Student(102, "Amit", 22, 78.5)
s3 = Student(103, "Sneha", 21, 92.0)


# Create College
c1 = College(3)


# Add students
c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)


# Display all students
print(c1)


# Get student
student = c1.GetStudent(102)

if student is not None:
    print("Student Found:")
    print(student)
else:
    print("Student Not Found")


# Remove student
c1.RemoveStudent(102)


# Display after removing
print("\nAfter Removing Student:")
print(c1)