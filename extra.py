# -*- coding: utf-8 -*-

n=input("输入一个小于1000的正整数：")
n=int(n)
a=0
a=int(a)
if n>1000:
    print("Error")
else:
    while n>1:
        if (n%2)==0:
             n=n/2
             a=a+1
        else:
             n=(3*n+1)/2
             a=a+1
    print(a)               
    
