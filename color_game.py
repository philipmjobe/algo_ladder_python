# Let’s try to make a game using Tkinter. In this game player has to enter color of the word that appears on the screen and hence the score increases by one, the total time to play this game is 30 seconds. Colors used in this game are Red, Blue, Green, Pink, Black, Yellow, Orange, White, Purple and Brown. Interface will display name of different colors in different colors. Player has to identify the color and enter the correct color name to win the game.


import tkinter
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0

timeleft = 30


def startGame(event):
    if timeleft == 30:
        countdown()

    nextColor()


def nextColor():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]))

        scoreLabel.config(text="Score: " + str(score))
