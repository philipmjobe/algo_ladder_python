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


def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)


root = tkinter.Tk()

root.title("COLORGAME")

root.geometry("375x200")

instructions = tkinter.Label(
    root, text="Type in the color" "of the words, and not the word text!", font=('Helvetica', 12))

instructions.pack()

scoreLabel = tkinter.Label(
    root, text="Press enter to start", font=('Helvetica', 12))

scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
