def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumaPrimos(a, b):
    return sum(i for i in range(a, b + 1) if esPrimo(i))

print(sumaPrimos(2, 12)) 