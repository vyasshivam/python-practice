# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:57:39 2017

@author: User
"""

import numpy

def drawBoard(_list):
    for x in range(0,3):
        print(' ---' * 3)
        a = ' '
        b = ' '
        c = ' '
        if _list[x][0] == 1:
            a = 'X'
        elif _list[x][0] == 2:
            a = 'O'
        else:
            a = ' '
            
        if _list[x][1] == 1:
            b = 'X'
        elif _list[x][1] == 2:
            b = 'O'
        else:
            b = ' '
            
        if _list[x][2] == 1:
            c = 'X'
        elif _list[x][2] == 2:
            c = 'O'
        else:
            c = ' '
        print('| %s | %s | %s |' % (a,b,c))
    print(' ---' * 3)


def checkHorizontal(_list):
    for x in _list:
        a = set(x)
        if len(a) == 1 and max(a) != 0:
            print('Player %s is wins' % (max(a)))
            return True
    return False
        
    
def checkDiagonal(_list):
    if(_list[1][1] != 0):
        if(_list[0][0] == _list[1][1] == _list[2][2]):
            print('Player %s is wins' % (_list[1][1]))
            return True
        elif(_list[0][2] == _list[1][1] == _list[2][0]):
            print('Player %s is wins' % (_list[1][1]))
            return True
            

def checkVertical(_list):
    _list = numpy.transpose(_list)
    for x in _list:
        a = set(x)
        if len(a) == 1 and max(a) != 0:
            print('Player %s is wins' % (max(a)))
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
        return False


if __name__ == "__main__":    
    game = [[0,0,0],[0,0,0],[0,0,0]]
    
    0,0
    count = 0
    winner = False

    while not winner:
        while not winner:
            player1 = input('Player1 please enter your coordinate : ')
            player1 = player1.split(',')
            if game[int(player1[0].strip())][int(player1[1].strip())] == 0 :
                count += 1
                game[int(player1[0].strip())][int(player1[1].strip())] = 1   
                drawBoard(game)
                winner = getWinner(game) 
                break
            else:
                print('Box is not empty. Enter again')
                drawBoard(game)
                
        if count == 9:        
            print('No Winner')
            break

        while not winner:   
            player2 = input('Player2 please enter your coordinate : ')
            player2 = player2.split(',')
            if game[int(player2[0].strip())][int(player2[1].strip())] == 0 :            
                count += 1
                game[int(player2[0].strip())][int(player2[1].strip())] = 2
                drawBoard(game)
                winner = getWinner(game)
                break
            else:
                print('Box is not empty. Enter again')
                drawBoard(game)