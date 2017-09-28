# -*- coding: utf-8 -*-
"""
Ask the user for a number and determine whether the number is prime or not. 
"""

def get_integer():
    return int(input('Please enter any number : '))

def is_prime(number):
    for x in range(2,number):
        if(number % x == 0):
            print('%s is not a prime number'%(number))
            return False
    return True

number = get_integer()
if(is_prime(number)):
    print('%s is a prime number'%(number))