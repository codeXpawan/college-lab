
import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


rectangle = Rectangle(3, 4)
print(f"Area of the rectangle: {rectangle.area()}")

circle = Circle(5)
print(f"Area of the circle: {circle.area()}")