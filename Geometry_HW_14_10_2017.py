import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("%.2f" % (0.5 * math.pi * (self.radius ** 2)))

    def perimeter(self):
        print("%.2f" % (2 * math.pi * self.radius))


class Rectangle:
    def __init__(self, length, width):
        self.a = length
        self.b = width

    def area(self):
        print("%.2f" % (self.a*self.b))


o = Circle(2)
o.area()
o.perimeter()

r = Rectangle(3,4)
r.area()
