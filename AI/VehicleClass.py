class Vehicle:
    def __init__(self,make,model) -> None:
        self.make = make
        self.model = model
        
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

car = Vehicle("Toyota", "Corolla")
car.drive()  

class Car(Vehicle):
    def drive(self):
        print(f"Driving the {self.make} {self.model} car")
        
car = Car("Toyota", "Corolla")
car.drive()