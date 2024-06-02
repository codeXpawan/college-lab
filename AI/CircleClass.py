import math

class Circle:
    def __init__(self,radius) -> None:
        self.__radius = radius
        self.area = self.calculate_area()
        self.permeter = self.calulate_perimeter()
        
    def calculate_area(self):
        return math.pi * self.__radius**2
    
    def calulate_perimeter(self):
        return 2*math.pi*self.__radius

circle = Circle(1)
print(f'The area of circle is {circle.area} and perimeter is {circle.permeter}')
    