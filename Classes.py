import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
       
    def area(self):
        return math.pi * self.__radius ** 2

c1 = Circle(7)
print(c1.area())        