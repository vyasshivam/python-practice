# -*- coding: utf-8 -*-
"""
Write a program that asks the user how many Fibonnaci numbers to generate and then 
generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def get_integer():
    return int(input('Enter a number : '))

a = []
for x in range(0,get_integer()):
    if(x==0):
        a.append(1)
    elif(x==1):
        a.append(1)
    else:
        a.append(a[-1] + a[-2])
print(a)