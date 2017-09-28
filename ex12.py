# -*- coding: utf-8 -*-
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes 
a new list of only the first and last elements of the given list. For practice, 
write this code inside a function.
"""

import random

def getList(_list):
    return [_list[0],_list[-1]]
list1 = random.sample(range(50),15)
print(list1)
print(getList(list1))