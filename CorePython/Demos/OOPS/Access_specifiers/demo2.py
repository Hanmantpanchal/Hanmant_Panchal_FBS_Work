class BusDriver:

    depoName = "Pune Depo"
    @staticmethod
    def setDepoName(Depo):
        BusDriver.depoName = Depo

    def __init__(self, DriverName, sal):
        self._DriverName = DriverName    
        self.__sal = sal                 

    # Getter
    def getSalary(self):
        return self.__sal

    # Setter
    def setSalary(self, sal):
        self.__sal = sal

   
  

    
    def display(self):
        print("Depo Name   :", BusDriver.depoName)
        print("Driver Name :", self._DriverName)
        print("Salary      :", self.__sal)



d1 = BusDriver("Hanmant", 35000)
d2 = BusDriver("Rahul", 40000)

print("Before Update")
d1.display()
print()
d2.display()


BusDriver.setDepoName("Nanded Depo")


d1.setSalary(45000)
print()

d1.display()
print()
d2.display()
  



# driver = BusDriver("Pune Depo", "Hanmant", 35000)

# print("Before Update")
# driver.display()

# # Update using Setters
# driver.setDriverName("Rahul")
# driver.setSalary(45000)

# # Update Static Variable
# BusDriver.changeCompany("Maharashtra State Road Transport")

# print("\nAfter Update")
# driver.display()

# # Access using Getters
# print("\nUsing Getters")
# print("Driver Name :", driver.getDriverName())
# print("Salary      :", driver.getSalary())