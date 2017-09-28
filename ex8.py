# -*- coding: utf-8 -*-
"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

import sys

player1 = input('Player 1 Enter R for Rock, S for Scissor or P for Paper : ')
player2 = input('Player 2 Enter R for Rock, S for Scissor or P for Paper : ')
if(player1 == player2):
    print('Match tied')
elif(player1.upper() == 'R'):
    if(player2.upper() == 'S'):
        print('Player 1 wins')
    elif(player2.upper() == 'P'):
        print('Player2 wins')
    else:
        print('Please enter proper input')
elif(player1.upper() == 'S'):
    if(player2.upper() == 'P'):
        print('Player 1 wins')
    elif(player2.upper() == 'R'):
        print('Player2 wins')
    else:
        print('Please enter proper input')
elif(player1.upper() == 'P'):
    if(player2.upper() == 'R'):
        print('Player 1 wins')
    elif(player2.upper() == 'S'):
        print('Player2 wins')
    else:
        print('Please enter proper input')
else:
    print('Please enter proper input')
    sys.exit;
            
    
               