# -*- coding: utf-8 -*-

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an 
appropriate message to the user. Hint: how does an even / odd number react differently
 when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

number = int(input('Enter any number : '))

   
if(number % 4 == 0):
    print('%s is multiple of 4'% (str(number)))
elif(number % 2 == 0):
    print('%s is even number'% (str(number)))
else:
    print('%s is odd number'% (str(number)))
 
    
num = int(input('Enter another number : '))
check = int(input('Enter a number you would like to divide above number with : '))
if(num % check == 0):
    print('%s is evenly divided by %s' % (str(num), str(check)))
else:
    print('%s is not evenly divided by %s' % (str(num), str(check)))
