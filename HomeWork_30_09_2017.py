def shiftArray():
    a = [0] * 10
    for i in range(10):
        a[i] = i
    print("Исходный массив:", a)
    b = a[9]
    for i in range(9, 0, -1):
        a[i] = a[i - 1]
    a[0] = b
    print("Сдвинутый массив:", a)


def arithmetic(a, b, c):
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        if b != 0:
            print(a / b)
        else:
            print("Ошибка деления")
    else:
        print("Неизвестная операция")


def divisors():
    a = int(input("Введите число:"))
    k = 0
    b = True
    if a < 0:
        a = -a
        b = False
    if a != 0:
        print("Делители числа:")
        for i in range(1, a + 1):
            if a % i == 0:
                k += 1
                print(i, -i)
    else:
        print("Делителями являются все целые числа, кроме 0")
    if b:
        return k
    else:
        return 0

def primeNumber():
    if divisors() == 2:
        print("Число простое")
    else:
        print("Число не является простым")


def palindrome():
    s = input("Введите строку:")
    b = True
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            b = False
            break
    if b:
        print("Строка полиндром")
    else:
        print("Строка не полиндром")


#shiftArray()
#arithmetic(1, 0, '//')
#divisors()
#palindrome()
primeNumber()
