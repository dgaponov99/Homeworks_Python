import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Площадь: ", "%.2f" % (0.5 * math.pi * (self.radius ** 2)))

    def perimeter(self):
        print("Периметр: ", "%.2f" % (2 * math.pi * self.radius))


class Rectangle:
    def __init__(self, length, width):
        self.a = length
        self.b = width

    def area(self):
        print("Площадь: ", "%.2f" % (self.a * self.b))


a = float(input("Введите радиус окружности: "))
o = Circle(a)
o.area()
o.perimeter()

print("Введите стороны прямоугольника:")
a = float(input())
b = float(input())
r = Rectangle(a, b)
r.area()
