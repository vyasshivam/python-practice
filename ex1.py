# -*- coding: utf-8 -*-
"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
import datetime

name = input('Enter you name : ')
age = int(input('Enter your age: '))

currentYear = datetime.datetime.now().year
print('In year %s %s will be 100 years old' % (str(currentYear - age + 100), name))
                        