# FILENAME: wordgames.py
# AUTHOR:   Robert James Patterson
# DATE:     04/26/2017
# SYNOPSIS: Word guessing game

import random

def get_random_word():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")

def get_guess():
    print("Enter a letter: ")
    return input()

def process_letter(letter, secret_word, blanked_word):    
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter
            
    return result

def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        print("X ", end="")
    print("")
    
def play_word_game():
    strikes = 0
    maxStrikes = 3
    playing = True
    
    word = get_random_word()
    blanked_word = list("_" * len(word))
    
    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)
            
        if strikes >= maxStrikes:
            playing = False

        if not "_" in blanked_word:
            playing = False
        
    if strikes >= maxStrikes:
        print("Loser!")
    else:
        print("Winner! The secret word was " + word)
    
#program execution
print("Game started")
play_word_game()
print("GAME OVER!")
