# -*- coding: utf-8 -*-
def nomalize(name):
    L=[]
    L.append(name)
    L=[i.lower() for i in L]
    L=[i.capitalize() for i in L]
    return L
L1=['adam','LISA','barT']
L2=list(map(nomalize,L1))
print(L2)
