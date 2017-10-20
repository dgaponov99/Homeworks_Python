def factorial(n):
    if n < 2:
        if n > 0:
            return n
        else:
            return 1
    else:
        return n * factorial(n - 1)


def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def pascalsTriangle(n):
    for i in range(n + 1):
        print(" " * (n - i), end='')
        for j in range(i + 1):
            print(C(i, j), end=' ')
        print("\n", end="")


pascalsTriangle(10)
