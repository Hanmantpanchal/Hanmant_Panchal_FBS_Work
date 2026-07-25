# Write a class program to set and get farmer details

class Farmer:

    def __init__(self, FarmerId, Name, AccountNumber, BankBranch, Age, LandArea, Income):
        self.FarmerId = FarmerId
        self.Name = Name
        self.AccountNumber = AccountNumber
        self.BankBranch = BankBranch
        self.Age = Age
        self.LandArea = LandArea
        self.Income = Income

    # Getter and Setter for FarmerId
    def getFarmerId(self):
        return self.FarmerId

    def setFarmerId(self, FarmerId):
        self.FarmerId = FarmerId

    # Getter and Setter for Name
    def getName(self):
        return self.Name

    def setName(self, Name):
        self.Name = Name

    # Getter and Setter for AccountNumber
    def getAccountNumber(self):
        return self.AccountNumber

    def setAccountNumber(self, AccountNumber):
        self.AccountNumber = AccountNumber

    # Getter and Setter for BankBranch
    def getBankBranch(self):
        return self.BankBranch

    def setBankBranch(self, BankBranch):
        self.BankBranch = BankBranch

    # Getter and Setter for Age
    def getAge(self):
        return self.Age

    def setAge(self, Age):
        self.Age = Age

    # Getter and Setter for LandArea
    def getLandArea(self):
        return self.LandArea

    def setLandArea(self, LandArea):
        self.LandArea = LandArea

    # Getter and Setter for Income
    def getIncome(self):
        return self.Income

    def setIncome(self, Income):
        self.Income = Income

    # Display Farmer Details
    def display(self):
        print("Farmer ID      :", p1.getFarmerId())
        print("Name           :", p1.getName())
        print("Account Number :", p1.getAccountNumber())
        print("Bank Branch    :", p1.getBankBranch())
        print("Age            :", p1.getAge())
        print("Land Area      :", p1.getLandArea())
        print("Income         :", p1.getIncome())


# Create Three Objects

p1 = Farmer(101, "Hanmant Panchal", 12345678901, "SBI Nanded", 23, "5 Acres", 350000)
p2 = Farmer(102, "Ashish Patil", 23456789012, "Bank of Maharashtra", 45, "8 Acres", 500000)
p3 = Farmer(103, "Soham Deshmukh", 34567890123, "HDFC Bank", 38, "6 Acres", 420000)


# Update Details using Setters

print()

p1.setFarmerId(201)
p1.setName("Rajesh Shinde")
p1.setAccountNumber(98765432109)
p1.setBankBranch("Union Bank Pune")
p1.setAge(30)
p1.setLandArea("10 Acres")
p1.setIncome(650000)

print()

p1.display()

p2.display()

p2.display()