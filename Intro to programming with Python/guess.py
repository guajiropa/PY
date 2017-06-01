# FILENAME: guess.py
# AUTHOR:   Robert James Patterson
# DATE:     04/26/2017
# SYNOPSIS: Number guessing game

import random

minNumber = 1
maxNumber = 100
found = False
magicNumber = random.randint(minNumber, maxNumber)

print('What is your favorite number?')
number = input()

print('Your favorite number is ' + number)

message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

while not found:
    print('Guess what the number is?')
    guess = int(input())
    if guess == magicNumber:
        found = True
    if guess < magicNumber:
        print("Too low")
    if guess > magicNumber:
        print("Too high")

print("You got it!")
        
        
