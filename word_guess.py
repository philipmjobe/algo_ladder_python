# This File will contain two examples of the word guessing game. These are code example walk throughs from geeksforgeeks.com


# Example 1: Word guessing game

# In this game, there is a list of words present, out of which our interpreter will choose 1 random word. The user first has to input their names and then, will be asked to guess any alphabet. If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. The user will be given 12 turns(which can be changed accordingly) to guess the complete word.

import random

name = input("What is your name? ")

print("Good Luck !", name)

words = [
    'rainbow',
    'computer',
    'science'
    'programming',
    'python',
    'mathematics',
    'player',
    'condition',
    'reverse',
    'water',
    'board',
    'geeks'
]

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            print(char, end=" ")
            failed += 1

        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break

        print()
        guess = input("guess a character:")

        guesses += guess

        if guess not in word:
            turns -= 1

            print("Wrong")

            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")
