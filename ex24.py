# -*- coding: utf-8 -*-
"""
http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
"""

def drawBoard(size):
    for x in range(0,size):
        print(' ---' * size)
        print('|   ' * (size + 1))
    print(' ---' * size)

if __name__ == "__main__":
    size = int(input('Enter the number of boxes: '))
    drawBoard(size)