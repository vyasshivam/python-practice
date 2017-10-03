# -*- coding: utf-8 -*-
"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
 to largest) and another number. The function decides whether or not the given number is inside the list and 
returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""
def search(_list, number):
    start = 0;
    end = len(_list) - 1
    while True:
        midIndex = round((start + end) / 2) + ((start + end) % 2)
        mid = _list[midIndex]
        print(mid)
        if(number == mid):
            return True
        elif(start == end - 1):
            return False
        elif(number < mid):
            end = midIndex
        elif(number > mid):
            start = midIndex
            
    

if __name__ == "__main__":
    _list = [1,2,4,5,6,9,10,15,18,21]
    number = int(input('Enter a number : '))
    if(search(_list, number)):
        print('%s exist in the list' % (number))
    else:
        print('%s do not exist in the list' % (number))