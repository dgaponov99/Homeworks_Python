def palindrome():
    s = input("Введите строку:")
    b = True
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            b = False
            break
    if b:
        print("Строка полиндром")
    else:
        print("Строка не полиндром")
