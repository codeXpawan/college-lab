class Engine:
    def __init__(self, type) -> None:
        self.type = type
    
    def start(self):
        print(f'{self.type} engine started. Brummm.....brummmm...')
    
    def stop(self):
        print(f'{self.type} engine stopped.')
        
class Wheel:
    def __init__(self, type):
        self.type = type
    
    def start(self):
        print(f'{self.type} wheel started rolling. Rollll...')
    
    def stop(self):
        print(f'{self.type} wheel stopped rolling.')
        
class Car:
    def __init__(self, engine_type, wheel_type) -> None:
        self.engine = Engine(engine_type)
        self.wheel = Wheel(wheel_type)
    
    def start_car(self):
        self.engine.start()
        print('Car started!')
        self.wheel.start()


car = Car("V8", "Alloy")
car.start_car()