# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):    
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return(x1,x2)
a=float(input("输入参数a:"))
b=float(input("输入参数b:"))
c=float(input("输入参数c:"))
x1,x2=quadratic(a,b,c)
print("x1=%s"% x1,"x2=%s"% x2)
