from util.util import extended_euclidean_inverse, modular_pow



class dh():
    def __init__(self, p=65537, g=3, x=None, y=None, X=None, Y=None, K1=None,K2= None):
        self.x = x
        self.y = y
        self.X = X
        self.Y = Y
        self.K1 = K1
        self.K2 = K2
        self.p = p
        self.g = g

    def getX(self):
        self.X= modular_pow(int(self.g), int(self.x), int(self.p))
        return self

    def getY(self):
        self.Y = modular_pow(int(self.g), int(self.y), int(self.p))
        return self

    def getK1(self):
        self.K1 = modular_pow(int(self.Y), int(self.x), int(self.p))
        return self

    def getK2(self):
        self.K2 = modular_pow(int(self.X), int(self.y), int(self.p))
        return self

