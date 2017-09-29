
"""

Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
“cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track
of the number of guesses the user makes throughout teh game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like this:
  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
"""
import random

def compareNumbers(number, userNumber):
    cows = 0
    bulls = 0
    for x in userNumber:
        if(x in number):
            bulls += 1
    for y in range(0,len(userNumber)):
        if(number[y] == userNumber[y]):
            cows += 1
    return('Cows - %s and Bulls - %s' %(cows, bulls))


if __name__=="__main__":
    number = str((random.randint(1000,9999)))   
    guessCount = 0
    while True:
        userNumber = str(input('Enter any 4 digit number : '))
        guessCount += 1
        if(number == userNumber):
            print('You guessed it correct after %s try' % (guessCount))
            break;
        else:
            print(compareNumbers(number, userNumber))
            

    