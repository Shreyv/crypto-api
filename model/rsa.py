from util.util import prime,extended_euclidean_inverse,modular_pow
import random
from math import pow


class rsa():
    def __init__(self,p = None,q= None,e= None,d= None,m = None,c = None,dm= None):
        self.p = p
        self.q = q
        self.e = e
        self.d = d
        self.m = m
        self.c = c
        self.dm = dm

    def get_random_numbers(self):
        prime_list = [x for x in range(1000,5000) if prime(x)]
        primes = random.sample(prime_list,2)
        self.p = primes[0]
        self.q = primes[1]
        return self

    def get_private_key(self):
        n = (self.p -1) * (self.q-1)
        inv = extended_euclidean_inverse(self.e,n)
        self.d = inv[1] % n
        return self
    def get_encryption(self):
        n = int(self.p) * int(self.q)
        self.c = (int(self.m) ** int(self.e)) % n
        return self
    def get_decryption(self):
        n = int(self.p) * (self.q)
        self.dm = modular_pow(int(self.c),int(self.d),n)
        return self

