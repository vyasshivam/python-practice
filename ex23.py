# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:42:06 2017

@author: User
"""

def fileToList(fileName):
    _list = []
    with open(fileName,'r') as file:
        line = file.readline()
        while line:        
            line = line.strip()
            _list.append(int(line))
            line = file.readline()
    return _list
    


if __name__ == "__main__" :    
    happyNumbers = fileToList('ex23_happyNumbers.txt')
    primeNumbers = fileToList('ex23_primeNumbers.txt')

    _list = []
    for x in primeNumbers:
        if(x in happyNumbers):
            _list.append(x)
            
    print(_list)