# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right.
 (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

randomNumber = random.randint(1,9)
end = False
guessedTime = 0
while not end:   
    
    userNumber = input('Guess a number between 1 to 9 or enter "exit" to exit ')
    if(userNumber.lower() == 'exit'):
        end = True
    elif(randomNumber == int(userNumber)):
        print('You guessed it right')
        end = True
    elif(randomNumber < int(userNumber)):        
        print('You guessed it too high')
    else:
        print('You guessed it too low')       
    guessedTime += 1 
print('After guessing %s times you got it right' %(guessedTime))