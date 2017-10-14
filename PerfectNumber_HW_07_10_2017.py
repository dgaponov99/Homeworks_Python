def perfectNumber(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
        if s > n:
            break
    if s == n:
        print("Yes")
    else:
        print("No")

perfectNumber(28)