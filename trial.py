# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:24:18 2017

@author: User
"""

count_dist = {}
with open('ex22_Training01.txt','r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        print(line.split('/')[2])
        break