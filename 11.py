# -*- coding: utf-8 -*-

L1= ['Hello','World',18,'Apple',None]
L2= [i.lower() for i in L1 if isinstance(i,str)==True]
print(L2)
