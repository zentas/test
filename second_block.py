import math

def is_prime(number):
    if number < 4:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(number))+1):
            if number % i == 0:
                return False
        return True

def square(a):
    return 4*a, a**2, a*math.sqrt(2)

def bank(a, years):
    return a * (1.1)**years
