import math

def is_prime(n):
    if n < 0:
        return "Os números negativos non están permitidos"
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def multiplicar(n, m):
    return n * m

def dividir(n, m):
    if m == 0:
        raise ValueError("Non se pode dividir por cero")
    return n / m

def cubic(a):
    return a * a * a

def say_hello(nome):
    return "Ola, " + nome
