# -*- coding: utf-8 -*-
"""
http://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
"""

import numpy

def checkHorizontal(_list):
    for x in _list:
        a = set(x)
        if len(a) == 1 and max(a) != 0:
            print('Player %s is winner' % (max(a)))
            return True
    return False
        
    
def checkDiagonal(_list):
    if(_list[1][1] != 0):
        if(_list[0][0] == _list[1][1] == _list[2][2]):
            print('Player %s is winner' % (_list[1][1]))
            return True
        elif(_list[0][2] == _list[1][1] == _list[2][0]):
            print('Player %s is winner' % (_list[1][1]))
            return True
            

def checkVertical(_list):
    _list = numpy.transpose(_list)
    for x in _list:
        a = set(x)
        if len(a) == 1 and max(a) != 0:
            print('Player %s is winner' % (max(a)))
            return True
    return False

def getWinner(_list):
    if checkHorizontal(_list):
        return True
    elif checkVertical(_list):
        return True
    elif checkDiagonal(_list):
        return True
    else:
        print('No Winner')
        return False


game1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
print('Result of game 1 : ')
getWinner(game1)


game2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
print('Result of game 2 : ')
getWinner(game2)

game3 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
print('Result of game 3 : ')
getWinner(game3)

game4 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]
print('Result of game 4 : ')
getWinner(game4)

game5 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]
print('Result of game 5 : ')
getWinner(game5)

game6 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
print('Result of game 6 : ')
getWinner(game6)