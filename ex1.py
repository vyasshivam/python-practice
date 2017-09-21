# -*- coding: utf-8 -*-
"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many 
   copies of the previous message.
"""
import datetime

name = input('Enter you name : ')
age = int(input('Enter your age: '))

currentYear = datetime.datetime.now().year
message = 'In year %s %s will be 100 years old' % (str(currentYear - age + 100), name)
print(message)

totalCopies = int(input('How many times you want to print the above message'))

#Print in one line
print(totalCopies * message)

#Print in new line
for x in range(0,totalCopies):
    print(message)