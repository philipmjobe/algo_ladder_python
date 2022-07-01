# This implementation of the mastermind game will have two sets of code one for easy and one for hard both taken and inputted by hand from geeksforgeeks


# Rules of the game
# Two players play the game against each other
# let’s assume Player 1 and Player 2.

# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# If Player 2 succeeds in his first attempt(despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# The game continues till Player 2 eventually is able to guess the number entirely.
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# If not, then Player 2 wins the game.
# The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons.

# We shall not be using any of the Pygame Libraries, to aid us with additional graphics, and therefore shall be dealing only with the framework and concept. Furthermore, we are going to be playing against the Computer i.e, the Computer would generate the number to be guessed.

import random

num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

if (n == num):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0

    while (n != num):
        ctr += 1
        count = 0

        n = str(n)

        num = str(num)

        correct = ['X'] * 4

        for i in range(0, 4):
            if (n[i] == num[i]):
                count += 1
                correct[i] = n[i]

            else:
                continue

        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ",
                  count, "digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=' ')
            print('\n')
            print('\n')
            n = int(input("Enter your next choice of numbers: "))

        elif (count == 0):
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    if n == num:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
