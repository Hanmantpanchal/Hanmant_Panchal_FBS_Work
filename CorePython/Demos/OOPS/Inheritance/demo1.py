class EMP:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSal(self):
        return self.sal

    def setSal(self, sal):
        self.sal = sal

    def display(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Salary : {self.sal}")


class HR(EMP):

    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com

    def getCommission(self):
        return self.com

    def setCommission(self, com):
        self.com = com

    def display(self):
        super().display()
        print(f"Commission : {self.com}")


class Developer(HR):

    def __init__(self, id, name, sal, com, incentive):
        super().__init__(id, name, sal, com)
        self.incentive = incentive

    def getIncentive(self):
        return self.incentive

    def setIncentive(self, incentive):
        self.incentive = incentive

    def display(self):
        super().display()
        print(f"Incentive : {self.incentive}")


# HR Objects
hr1 = HR(101, "Rahul", 50000, 7000)
hr2 = HR(102, "Amit", 55000, 8000)
hr3 = HR(103, "Priya", 60000, 9000)

# Developer Objects
dev1 = Developer(201, "Hanmant", 50000, 7000, 10000)
dev2 = Developer(202, "Ashish", 55000, 8000, 12000)
dev3 = Developer(203, "Rajwardhan", 60000, 9000, 15000)

print(" HR Details ")

hr1.display()

print()

print("Developer Details")

dev1.display()








        

