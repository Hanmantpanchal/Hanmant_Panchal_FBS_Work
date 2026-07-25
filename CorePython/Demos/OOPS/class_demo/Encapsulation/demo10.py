# Write a class program to set and get laptop details

class Laptop:

    # Constructor
    def __init__(self, LaptopId, Brand, Model, Processor, RAM, Price):
        self.LaptopId = LaptopId
        self.Brand = Brand
        self.Model = Model
        self.Processor = Processor
        self.RAM = RAM
        self.Price = Price

    # Getter and Setter for LaptopId
    def getLaptopId(self):
        return self.LaptopId

    def setLaptopId(self, LaptopId):
        self.LaptopId = LaptopId

    # Getter and Setter for Brand
    def getBrand(self):
        return self.Brand

    def setBrand(self, Brand):
        self.Brand = Brand

    # Getter and Setter for Model
    def getModel(self):
        return self.Model

    def setModel(self, Model):
        self.Model = Model

    # Getter and Setter for Processor
    def getProcessor(self):
        return self.Processor

    def setProcessor(self, Processor):
        self.Processor = Processor

    # Getter and Setter for RAM
    def getRAM(self):
        return self.RAM

    def setRAM(self, RAM):
        self.RAM = RAM

    # Getter and Setter for Price
    def getPrice(self):
        return self.Price

    def setPrice(self, Price):
        self.Price = Price

    # Display Laptop Details
    def display(self):
        print("Laptop ID :", self.getLaptopId())
        print("Brand     :", self.getBrand())
        print("Model     :", self.getModel())
        print("Processor :", self.getProcessor())
        print("RAM       :", self.getRAM())
        print("Price     :", self.getPrice())



p1 = Laptop(101, "Dell", "Inspiron 15", "Intel Core i5", "16GB", 65000)
p2 = Laptop(102, "HP", "Pavilion 14", "AMD Ryzen 5", "8GB", 58000)
p3 = Laptop(103, "Lenovo", "IdeaPad Slim 5", "Intel Core i7", "16GB", 72000)



print()

p1.display()

print()

p2.display()

print()

p3.display()

p2.setBrand("ACER")

print()
print(p2.getBrand())

p2.display()

