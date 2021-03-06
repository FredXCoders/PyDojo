'''
guess.py

This is a simple number guessing game taken from the book:
"Invent Your Own Computer Games with Python", 2nd Edition
By Al Sweigart

http://inventwithpython.com/
'''
import random

guessesTaken = 0
myName = raw_input('Hello! What is your name?')

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

