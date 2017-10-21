class RimTranslator:
    characters = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    numbers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    def toRim(self, n):
        if 0 < n < 4000:
            rim = ''
            i = 0
            while n > 0:
                while n >= self.numbers[i]:
                    n -= self.numbers[i]
                    rim += self.characters[i]
                i += 1
            return rim
        else:
            print("Ошибка ввода")

    def toArab(self, s):
        n = 0
        i = 0
        j = 0
        while j < 13:
            while s[i:i + len(self.characters[j])] == self.characters[j]:
                n += self.numbers[j]
                i += len(self.characters[j])
            j += 1
        return n


t = RimTranslator()
print("Введите натуральное число: ", end='')
a = int(input())
print("Римская система счисления: ", t.toRim(a))
print("Введите число в римской СС: ", end='')
b = input()
print("Арабская система счисления: ", t.toArab(b))


