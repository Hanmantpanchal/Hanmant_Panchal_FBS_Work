class Watch:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Getter and Setter for Brand
    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    # Getter and Setter for Model
    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    # Getter and Setter for Price
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    # Display Method
    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)


# Derived Class 1

class AnalogWatch(Watch):

    def __init__(self, brand, model, price, strapMaterial):
        super().__init__(brand, model, price)
        self.strapMaterial = strapMaterial

    # Getter and Setter
    def getStrapMaterial(self):
        return self.strapMaterial

    def setStrapMaterial(self, strapMaterial):
        self.strapMaterial = strapMaterial

    def display(self):
        super().display()
        print("Strap Material :", self.strapMaterial)


# Derived Class 2

class SmartWatch(Watch):

    def __init__(self, brand, model, price, operatingSystem):
        super().__init__(brand, model, price)
        self.operatingSystem = operatingSystem

    # Getter and Setter
    def getOperatingSystem(self):
        return self.operatingSystem

    def setOperatingSystem(self, operatingSystem):
        self.operatingSystem = operatingSystem

    def display(self):
        super().display()
        print("Operating System :", self.operatingSystem)


# Creating Objects

analog1 = AnalogWatch("Titan", "Neo", 3500, "Leather")
analog2 = AnalogWatch("Fastrack", "Reflex", 2500, "Metal")

smart1 = SmartWatch("Apple", "Watch Series 10", 49999, "watchOS")
smart2 = SmartWatch("Samsung", "Galaxy Watch 7", 29999, "Wear OS")


print("Analog Watches")
analog1.display()
print()
analog2.display()

print()

print("Smart Watches")
smart1.display()
print()
smart2.display()