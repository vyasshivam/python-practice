# -*- coding: utf-8 -*-
"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""
string = input('Enter any word : ')
if(string == string[::-1]):
    print('%s is palindrome' %(string))
else:
    print('%s is not palindrome' %(string))
    
