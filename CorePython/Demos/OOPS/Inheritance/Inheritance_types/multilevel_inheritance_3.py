#multilevel inheritance 

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def displayVehicle(self):
        print(f"Brand : {self.brand}")


class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def displayCar(self):
        self.displayVehicle()
        print(f"Model : {self.model}")


class SportsCar(Car):

    def __init__(self, brand, model, topSpeed):
        super().__init__(brand, model)
        self.topSpeed = topSpeed

    def display(self):
        self.displayCar()
        print(f"Top Speed : {self.topSpeed} km/h")


car = SportsCar("Ferrari", "F8", 340)
car.display()