class Student:

    def __init__(self, studentID, studentName, dept, marks):
        self.StudentID = studentID
        self.StudentName = studentName
        self.Dept = dept
        self.Marks = marks

    # Getter Methods
    def getStudentID(self):
        return self.StudentID

    def getStudentName(self):
        return self.StudentName

    def getDept(self):
        return self.Dept

    def getMarks(self):
        return self.Marks

    # Setter Methods
    def setStudentName(self, name):
        self.StudentName = name

    def setMarks(self, marks):
        if 0 <= marks <= 100:
            self.Marks = marks
        else:
            print("Invalid Marks")


# User Input
id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
dept = input("Enter Department: ")
marks = int(input("Enter Marks: "))

# Create Object
student1 = Student(id, name, dept, marks)

# Display using Getters
print("\nStudent Details")
print("ID:", student1.getStudentID())
print("Name:", student1.getStudentName())
print("Department:", student1.getDept())
print("Marks:", student1.getMarks())

# Update using Setters
new_name = input("\nEnter New Name: ")
student1.setStudentName(new_name)

new_marks = int(input("Enter New Marks: "))
student1.setMarks(new_marks)

# Display Updated Details using Getters
print("\nUpdated Student Details")
print("ID:", student1.getStudentID())
print("Name:", student1.getStudentName())
print("Department:", student1.getDept())
print("Marks:", student1.getMarks())