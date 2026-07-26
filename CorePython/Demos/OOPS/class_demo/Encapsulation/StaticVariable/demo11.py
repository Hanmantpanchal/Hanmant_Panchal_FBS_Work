class student:
    collageName = "Firstbit solution"  # Static Variable 
    def __init__(self , StudentID , Name  , Class  , Marks ):
        self. StudentID  = StudentID
        self.Name = Name
        self.Class = Class
        self.Marks = Marks

    def getStudentID(self):
        return self.StudentID
    def setStudentID(self , StudentID):
        self.StudentID = StudentID


    def getName(self):
        return self.Name
    def setName(self ,Name ):
        self.Name = Name


    def getClass(self):
        return self.Class
    def setClass(self , Class):
        self.Class = Class

    def getMarks(self):
        return self.Marks
    def setMarks(self , Marks):
        self.Marks = Marks


    def setCollageName(student  , CollageName):
           student.collageName = CollageName


    def Display(self):
        print(f"StudentID : {self.StudentID}")
        print(f"Name : {self.Name}")
        print(f"Class : {self.Class}")
        print(f"Marks : {self.Marks}")
        print(f"Collage Name : {student.collageName}") #It is a static variable so we should call the static variable through class name  

ID = int(input("Enter the student ID :"))
NAME = input("Enter the student Name :")
classroom = input("Enter the class :") 
marks = int(input("Enter the Marks :"))

student1 = student(ID , NAME , classroom , marks)

print()
student1.Display()

