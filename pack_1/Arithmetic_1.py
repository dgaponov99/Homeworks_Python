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