# -*- encoding: utf-8 -*-

import os

def printfile(tips,path='.'):
    l=path
    for x in os.listdir(path):  #遍历当前所有目录
        if os.path.isdir(x):
            printfile(tips,path=os.path.join(l,x))
        else:
            if x.find(tips) != -1:
                print(os.path.join(l,x))
                    
b=str(input('输入需要查找的字符串：'))
printfile(b)
