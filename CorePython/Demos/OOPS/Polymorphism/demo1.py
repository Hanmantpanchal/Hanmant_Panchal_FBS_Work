class EMP:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    # Getter Methods
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getSalary(self):
        return self.sal

    # Setter Methods
    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setSalary(self, sal):
        self.sal = sal

    # Calculate Salary
    def calculateSalary(self):
        print(f"Final Salary : {self.sal}")

    # Display
    def display(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Basic Salary : {self.sal}")
        self.calculateSalary()


class HR(EMP):

    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal)
        self.commission = commission

    # Getter
    def getCommission(self):
        return self.commission

    # Setter
    def setCommission(self, commission):
        self.commission = commission

    # Method Overriding
    def calculateSalary(self):
        total = self.sal + self.commission
        print(f"Final Salary : {total}")

    # Display
    def display(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Basic Salary : {self.sal}")
        print(f"Commission : {self.commission}")
        self.calculateSalary()


class Developer(EMP):

    def __init__(self, id, name, sal, incentive):
        super().__init__(id, name, sal)
        self.incentive = incentive

    # Getter
    def getIncentive(self):
        return self.incentive

    # Setter
    def setIncentive(self, incentive):
        self.incentive = incentive

    # Method Overriding
    def calculateSalary(self):
        total = self.sal + self.incentive
        print(f"Final Salary : {total}")

    # Display
    def display(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Basic Salary : {self.sal}")
        print(f"Incentive : {self.incentive}")
        self.calculateSalary()


# Objects
emp1 = EMP(100, "Rohan", 30000)
hr1 = HR(101, "Rahul", 50000, 7000)
dev1 = Developer(201, "Hanmant", 60000, 10000)

print("EMP Details")
emp1.display()

print()

print("HR Details")
hr1.display()

print()
print("Developer Details")
dev1.display()