# Python is a multipurpose language and one can do anything with it. Python can also be used for game development. Let’s create a simple command-line Rock-Paper-Scissor game without using any external game libraries like PyGame. In this game, the user gets the first chance to pick the option between Rock, paper, and scissors. After the computer select from the remaining two choices(randomly), the winner is decided as per the rules.

import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    print("Enter choice \n 1 for Rock, \n 2 for Paper, and \n 3 for scissor \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter vaild input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'scissor'

    print("user choice is: " + choice_name)
    print("\nNow its computer turn........")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    result = ""

    if choice == comp_choice:
        print("Draw=> ", end="")
        result = Draw

        if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
            print("Paper wins =>", end="")
            result = "Paper"

        elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end="")
            result = "Rock"

        else:
            print("scissor wins =>", end="")
            result = "scissor"

    if result == Draw:
        print("<== Its a tie ==>")

    if result == choice_name:
        print("<== User wins ==>")

    else:
        print("<== Computer Wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower

    if ans == 'n':
        break

print("\mThanks for playing")
