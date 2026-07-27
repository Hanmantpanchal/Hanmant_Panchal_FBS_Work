#single inheritance 

class Vehicle:
    def __init__(self , brand  , model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"BrandName :{self.brand}")
        print(f"ModelName :{self.model}")

class car(Vehicle):
    def __init__(self, brand, model , Fueltype):
        super().__init__(brand, model)
        self.Fueltype = Fueltype
    def display(self):
        super().display()
        print(f"fuelt type :{self.Fueltype}")


car1 = car("Toyota" , "Fortuner" , "disel")
car1.display()
    