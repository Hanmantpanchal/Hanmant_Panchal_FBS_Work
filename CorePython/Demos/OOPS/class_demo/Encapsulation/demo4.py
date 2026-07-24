class Student:

    def __init__(self, studentID, studentName, dept, marks):
        self.StudentID = studentID
        self.StudentName = studentName
        self.Dept = dept
        self.Marks = marks

    # Getters
    def getStudentID(self):
        return self.StudentID

    def getStudentName(self):
        return self.StudentName

    def getDept(self):
        return self.Dept

    def getMarks(self):
        return self.Marks


# User Input
a = input("Enter Student ID: ")
b = input("Enter Student Name: ")
c = input("Enter Department: ")
d = int(input("Enter Marks: "))

# Object
student1 = Student(a, b, c, d)

# Output using getters
print("Student ID :", student1.getStudentID())
print("Student Name :", student1.getStudentName())
print("Department :", student1.getDept())
print("Marks :", student1.getMarks())