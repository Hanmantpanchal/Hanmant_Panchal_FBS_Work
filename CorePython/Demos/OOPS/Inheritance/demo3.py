# Base Class
class Computer:

    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram

    # Getter and Setter for Brand
    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    # Getter and Setter for Processor
    def getProcessor(self):
        return self.processor

    def setProcessor(self, processor):
        self.processor = processor

    # Getter and Setter for RAM
    def getRam(self):
        return self.ram

    def setRam(self, ram):
        self.ram = ram

    # Display Method
    def display(self):
        print("Brand :", self.brand)
        print("Processor :", self.processor)
        print("RAM :", self.ram)


# Derived Class 1
class DesktopComputer(Computer):

    def __init__(self, brand, processor, ram, cabinetType):
        super().__init__(brand, processor, ram)
        self.cabinetType = cabinetType

    # Getter and Setter
    def getCabinetType(self):
        return self.cabinetType

    def setCabinetType(self, cabinetType):
        self.cabinetType = cabinetType

    def display(self):
        super().display()
        print("Cabinet Type :", self.cabinetType)


# Derived Class 2
class Laptop(Computer):

    def __init__(self, brand, processor, ram, batteryCapacity):
        super().__init__(brand, processor, ram)
        self.batteryCapacity = batteryCapacity

    # Getter and Setter
    def getBatteryCapacity(self):
        return self.batteryCapacity

    def setBatteryCapacity(self, batteryCapacity):
        self.batteryCapacity = batteryCapacity

    def display(self):
        super().display()
        print("Battery Capacity :", self.batteryCapacity)




desktop1 = DesktopComputer("Dell", "Intel i5", "16 GB", "Tower")
desktop2 = DesktopComputer("HP", "Intel i7", "32 GB", "Mini Tower")

laptop1 = Laptop("Lenovo", "Ryzen 5", "16 GB", "65 Wh")
laptop2 = Laptop("Asus", "Intel i9", "32 GB", "90 Wh")

print("Desktop")

desktop1.display()


desktop2.display()

print()

print("Laptop")


laptop1.display()


laptop2.display()