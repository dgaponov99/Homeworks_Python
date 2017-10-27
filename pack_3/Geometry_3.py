import math


class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print("Площадь: ", "%.2f" % (self.a * self.b))


class Circle(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        print("Площадь: ", "%.2f" % (0.5 * math.pi * (self.a ** 2)))

    def perimeter(self):
        print("Периметр: ", "%.2f" % (2 * math.pi * self.a))


a = float(input("Введите радиус окружности: "))
o = Circle(a)
o.area()
o.perimeter()

print("Введите стороны прямоугольника:")
a = float(input())
b = float(input())
r = Rectangle(a, b)
r.area()
