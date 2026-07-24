#1. Student Management System

class student:
    def __init__(self , studentID , StudentName , Dept , Marks):
        self.StudentID = studentID
        self.StudentName = StudentName
        self.Dept = Dept
        self.Marks = Marks

    # def getStudentID(self):
    #     return self.StudentID
    # def getStudentID(self):
    #     return self.StudentName
    # def getStudentID(self):
    #     return self.Dept
    # def getStudentID(self):
    #     return self.Marks

    def display(self):
        print(f"ID = {self.StudentID}")
        print(f"Name = {self.StudentName}")
        print(f"Department = {self.Dept}")
        print(f"Marks = {self.Marks}")

a = input("Enter the StudentID :")
b = input("Enter the StudentName :")
c = input("Enter the Student Department :")
d = int(input("Enter the student marks :"))



student1 = student(a , b ,c , d )

student1.display()