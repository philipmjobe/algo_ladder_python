# Task: Below are the steps:

# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random
import math

lower = int(input("Enter Lower Bound:- "))

upper = int(input("Enter Upper Bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")


count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a numbeer:- "))

    if x == guess:
        print("Congratulations you did it in", count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
