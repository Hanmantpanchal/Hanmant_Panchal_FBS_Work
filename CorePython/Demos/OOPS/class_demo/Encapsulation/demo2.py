class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    # Getter and Setter for ID
    def getId(self):
        return self.id

    # def setId(self, id):
    #     self.id = id

    # Getter and Setter for Name
    def getName(self):
        return self.name

    # def setName(self, name):
    #     self.name = name

    # Getter and Setter for Salary
    def getSalary(self):
        return self.sal

    # def setSalary(self, sal):
    #     self.sal = sal

    # Display Method
    def display(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Salary = {self.sal}")


# Create Object
e1 = Emp(101, "Hanmant", 123456)

# Display Details
# e1.display()

# # Using Getters
print("\nUsing Getters")
print("ID:", e1.getId())
# print("Name:", e1.getName())
# print("Salary:", e1.getSalary())

# # Using Setters
# e1.setId(102)
# e1.setName("Rahul")
# e1.setSalary(50000)

# print("\nAfter Updating")
# e1.display()