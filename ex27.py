# -*- coding: utf-8 -*-
"""
http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
"""

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

count = 0

while True:
    while True:
        count += 1
        player1 = input('Player1 please enter your coordinate : ')
        player1 = player1.split(',')
        if game[int(player1[0].strip())][int(player1[1].strip())] == 0 :
            game[int(player1[0].strip())][int(player1[1].strip())] = 1
            break
        else:
            print('Box is not empty. Enter again')
        print(count)
        
    if count == 9:
        break

    while True:        
        count += 1
        player2 = input('Player2 please enter your coordinate : ')
        player2 = player2.split(',')
        if game[int(player2[0].strip())][int(player2[1].strip())] == 0 :
            game[int(player2[0].strip())][int(player2[1].strip())] = 2
            break
        else:
            print('Box is not empty. Enter again')
        print(count)
        
print(game)
    