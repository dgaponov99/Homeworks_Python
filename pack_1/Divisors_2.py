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
