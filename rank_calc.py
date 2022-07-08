# Python offers multiple options for developing a GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. In this article, we will learn how to create a Rank Based – Percentile Gui Calculator application using Tkinter, with a step-by-step guide.
# To create a Tkinter:

# Importing the module – Tkinter
# Create the main window (container)
# Add any number of widgets to the main window.
# Apply the event Trigger on the widgets.

from tkinter import *


def getPercentile():
    students = int(total_participantField.get())

    rank = int(rankField.get())

    result = round((students - rank) / students * 100, 3)

    percentileField.insert(10, str(result))


def Clear():
    rankField.delete(0, END)

    total_participantField.delete(0, END)

    percentileField.delete(0, END)


if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="light green")

    gui.title("Rank Based- Percentile Calculator")

    gui.geometry("950x200")

    rank = Label(gui, text="Rank", bg="blue")
    and1 = Label(gui, text="And", bg="blue")

    total_participant = Label(gui, text="Total Participants", bg="blue")

    find = Button(gui, text="Find Percentile", fg="black",
                  bg="red", command=getPercentile)

    percentile = Label(gui, text="Percentile", bg="blue")

    clear = Button(gui, text="Clear", fg="black", bg="red", command=Clear)

    rank.grid(row=1, column=1, padx=10)

    and1.grid(row=1, column=4)

    total_participant.grid(row=1, column=6, padx=10)

    find.grid(row=3, column=6, pady=10)

    percentile.grid(row=4, column=3, padx=10)

    clear.grid(row=5, column=3, pady=10)

    rankField = Entry(gui)

    total_participantField = Entry(gui)

    percentileField = Entry(gui)

    rankField.grid(row=1, column=2)

    total_participantField.grid(row=1, column=7)

    percentileField.grid(row=4, column=4)

    gui.mainloop()
