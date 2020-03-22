from util.util import extended_euclidean_inverse, modular_pow


class uegr():
    def __init__(self,p=65537, g=3, x=None, y=None, m=None, c1=None, c2=None, c3=None, c4=None,
     r1=None,r2=None, s=None, t=None,c1_=None, c2_=None, c3_=None, c4_=None):
       
       self.p = p
       self.g = g
       self.x = x
       self.y = y
       self.m = m
       self.c1 = c1
       self.c2 = c2
       self.c3 = c3
       self.c4 = c4
       self.r1 = r1
       self.r2 = r2
       self.s = s
       self.t = t
       self.c1_ = c1_
       self.c2_ = c2_
       self.c3_ = c3_
       self.c4_ = c4_

    def get_public_key(self,obj):
        obj['y'] = modular_pow(int(obj['g']), int(obj['x']), int(obj['p']))
        return obj

    def get_c2(self,obj):
        obj['c2'] = modular_pow(int(obj['y']), int(obj['r1']), int(obj['p']))
        obj['c2'] = modular_pow(int(obj['m']) * int(obj['c2']), 1, int(obj['p'])) 
        return obj

    def get_c1(self,obj):
        obj['c1'] = modular_pow(int(obj['g']), int(obj['r1']), int(obj['p']))
        return obj

    def get_c3(self,obj):
        obj['c3'] = modular_pow(int(obj['g']), int(obj['r2']), int(obj['p']))
        return obj

    def get_c4(self,obj):
        obj['c4'] = modular_pow(int(obj['y']), int(obj['r2']), int(obj['p']))
        return obj   

    def get_c2_(self,obj):
        obj['c2_'] = (int(obj['m']) * (int(obj['m']) * modular_pow(int(obj['y']), int(obj['r1'])+ (int(obj['r2'])* int(obj['s'])), int(obj['p']))) % int(obj['p'])) % int(obj['p'])
        return obj

    def get_c1_(self,obj):
        obj['c1_'] = modular_pow(int(obj['g']), int(obj['r1'])+(int(obj['r2']) * int(obj['s'])), int(obj['p']))
        return obj

    def get_c3_(self,obj):
        obj['c3_'] = modular_pow(int(obj['g']), int(obj['r2']) * int (obj['t']), int(obj['p']))
        return obj

    def get_c4_(self,obj):
        obj['c4_'] = modular_pow(int(obj['y']), int(obj['r2']) * int (obj['t']), int(obj['p']))
        return obj     



