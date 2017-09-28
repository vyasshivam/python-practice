# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:29:35 2017

@author: User
"""

import random

def passwordGenerator(size):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_{}:<>?[];',./||"
    pswd = ""
    for i in range(size):
        pswd += letters[random.randrange(len(letters))]
    return pswd

print(passwordGenerator(int(input('How many characters in your password?'))))