# -*- coding: utf-8 -*-
"""
http://www.practicepython.org/solution/2016/07/16/28-max-of-three-solutions.html
"""
def getMaximum(a,b,c):
    if(a>b & a>c):
        return str(a) + ' is maximum of all'
    elif(b>a & b>c):
        return str(b) + ' is maximum of all'
    else:
        return str(c) + ' is maximum of all'
        
a = int(input('Enter 1st number :'))
b = int(input('Enter 2nd number :'))
c = int(input('Enter 3rd number :'))
print(getMaximum(a,b,c))