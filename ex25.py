# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:21:04 2017

@author: User
"""

_list = []
for x in range(0,100):
    _list.append(x)

start = 0
end = len(_list) - 1
guessCount = 0
while True:
    guessCount += 1
    midIndex = round((start + end) / 2) + ((start + end) % 2)
    mid = _list[midIndex]
    print('Your number is : '+str(mid))
    guessed = input('Enter h for high , l for low and c for correct gueess ')
    
    if guessed == 'c':
        print('It took %s try to guess it correctly' % (guessCount))
        break
    elif guessed == 'h':
        end = midIndex
    elif guessed == 'l':
        start = midIndex