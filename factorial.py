def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fact(n): return 1 if n <= 1 else n * fact(n - 1)


print(factorial(4))
print(fact(8))
