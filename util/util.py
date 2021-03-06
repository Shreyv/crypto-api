from math import sqrt
import math


def prime(x):
    if x % 2 == 0:
        return False
    elif any(x % i == 0 for i in range(3, int(sqrt(x)) + 1, 2)):
        return False
    else:
        return True


def extended_euclidean_inverse(a, b):
    a = int(a)
    b = int(b)
    if a == 0:
        return (b, 0, 1)
    else:
        div = b // a
        rem = b % a
        n, r1, d1 = extended_euclidean_inverse(rem, a)
        return (n, d1 - div * r1, r1)


def modular_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def modInverse(b,m): 
    g = math.gcd(b, m)  
    if (g != 1): 
        return -1
    else:   
        return pow(b, m - 2, m) 
  
   
def modDivide(a,b,m): 
    a = a % m 
    inv = modInverse(b,m) 
    if(inv == -1): 
        return -1
    else: 
        return (inv*a) % m
