from  model.eg import eg
from util.util import extended_euclidean_inverse, modular_pow


class egr():
    def __init__(self,c1_= None,c2_= None,s= None):
        self.c1_ = c1_
        self.c2_ = c2_
        self.s = s

    def get_public_key(self,obj):
        obj['eg1'] = eg(x = obj['eg1']['x']).__dict__
        print(obj)
        obj['eg1']['y'] = modular_pow(int(obj['eg1']['g']), int(obj['eg1']['x']), int(obj['eg1']['p']))
        return obj

    def getc1(self,obj):
        obj['eg1']['c1'] = modular_pow(int(obj['eg1']['g']), int(obj['eg1']['r']), int(obj['eg1']['p']))
        return obj

    def getc2(self,obj):
        obj['eg1']['c2'] = int(obj['eg1']['m']) * modular_pow(int(obj['eg1']['y']), int(obj['eg1']['r']), int(obj['eg1']['p']))
        return obj

    def get_reencryption(self,obj):
        obj['c1_'] = modular_pow(int(obj['eg1']['g']), int(obj['eg1']['r'])+int(obj['s']), int(obj['eg1']['p']))
        obj['c2_']= int(obj['eg1']['m']) * modular_pow(int(obj['eg1']['y']), int(obj['eg1']['r'])+int(obj['s'])  , int(obj['eg1']['p']))
        return obj