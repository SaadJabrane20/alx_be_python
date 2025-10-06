from math import pi

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self,length,width):
        self.legnth = length
        self.width = width

    def area(self):
        return self.legnth * self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius
