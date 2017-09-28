# -*- coding: utf-8 -*-
"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of
 the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

def removeDup1(list1):
    newList = []
    for x in list1:
        if not x in newList:
            newList.append(x)
    return newList

def removeDup2(list1):
    return set(list1)

a = [1,2,5,4,6,2,4,5,3,1,9,8,7,4,1]

print(removeDup1(a))
print(removeDup2(a))