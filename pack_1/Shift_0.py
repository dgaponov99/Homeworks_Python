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