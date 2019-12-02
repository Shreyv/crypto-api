from util.util import extended_euclidean_inverse, modular_pow



class eg():
    def __init__(self, p=65537, g=3, x=None, y=None, m=None, c1=None, c2=None, dm=None, r=None):
        self.x = x
        self.y = y
        self.m = m
        self.c1 = c1
        self.c2 = c2
        self.dm = dm
        self.r = r
        self.p = p
        self.g = g

    def get_public_key(self):
        self.y = modular_pow(int(self.g), int(self.x), int(self.p))
        return self

    def getc1(self):
        self.c1 = modular_pow(int(self.g), int(self.r), int(self.p))
        return self

    def getc2(self):
        self.c2 = int(self.m) * modular_pow(int(self.y), int(self.r), int(self.p))
        return self

    def get_decryption(self):
        K = modular_pow(int(self.c1), int(self.x), int(self.p))
        temp = extended_euclidean_inverse(K, self.p)
        self.dm = (int(self.c2) * (temp[1] % self.p)) % self.p
        return self
