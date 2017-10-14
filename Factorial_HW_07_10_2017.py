def factorialCycle(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

def factorialRec(n):
    if n < 2:
        return(n)
    else:
        return(n*factorialRec(n-1))

factorialCycle(6)
print(factorialRec(5))