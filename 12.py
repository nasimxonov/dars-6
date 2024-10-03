# math_utils.py

def kvadrat(n):
    return n ** 2

def kub(n):
    return n ** 3

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f

print(kvadrat(4))

print(kub(5))

print(faktorial(400))