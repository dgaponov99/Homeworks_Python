class Polynomial:
    def __init__(self, p):
        self.p = p
        self.ratio = []
        self.degree = []
        self.__cast()

    def __cast(self):
        s = str(self.p)
        ratio = list(self.ratio)
        degree = list(self.degree)
        list_poly = []

        while len(s) > 0:
            a = s.rfind('+')
            if a < s.rfind('-'):
                a = s.rfind('-')
            if a > -1:
                list_poly.append(s[a:])
                s = s[:a]
            elif len(s) > 0:
                list_poly.append(s)
                break

        for i in range(len(list_poly)):
            s = str(list_poly.pop())
            if s.find('x') == -1:
                ratio.append(float(s))
                degree.append(0)
            elif s.find('^') > 0:
                if s.find('x') == 0:
                    ratio.append(1)
                elif s[s.find('x') - 1] == '+':
                    ratio.append(1)
                elif s[s.find('x') - 1] == '-':
                    ratio.append(-1)
                else:
                    ratio.append(float(s[:s.find('x')]))
                degree.append(int(s[s.find('^') + 1:]))
            else:
                if s.find('x') == 0:
                    ratio.append(1)
                elif s[s.find('x') - 1] == '+':
                    ratio.append(1)
                elif s[s.find('x') - 1] == '-':
                    ratio.append(-1)
                else:
                    ratio.append(float(s[:-1]))
                degree.append(1)
        self.ratio = ratio
        self.degree = degree

    def derivative(self):
        der = ''
        l = len(self.ratio)
        for i in range(l):
            prob = ''
            a = self.ratio.pop(0)
            k = self.degree.pop(0)
            a1 = self.floatToInt(a * k)
            k1 = (k - 1)

            if a1 > 0 and i > 0:
                prob = '+'

            if a1 == 0:
                pass
            elif k1 == 0:
                if a1 == 1 and i > 0:
                    a1 = '+'
                elif a1 == 1:
                    a1 = ''
                elif a1 == -1:
                    a1 = '-'
                der += prob + str(a1)
            else:
                if a1 == 1 and i > 0:
                    a1 = '+'
                elif a1 == 1:
                    a1 = ''
                elif a1 == -1:
                    a1 = '-'
                if k1 != 1:
                    der += prob + str(a1) + 'x^' + str(k1)
                else:
                    der += prob + str(a1) + 'x'

        return der

    @staticmethod
    def floatToInt(value):
        if value - int(value) == 0:
            return int(value)
        else:
            return value


print('Пример полинома: 0.25x^4-6x^3+x^2-2x+7')
s = input('Введите полином: ')
p = Polynomial(s)
print('Производная: ' + p.derivative())
