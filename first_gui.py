from tkinter import *

root = Tk()

root.title("Welcome")

root.geometry('350x200')

lbl = Label(root, text="Howdy")
lbl.grid()


def clicked():
    lbl.configure(text="I've been clicked")


btn = Button(root, text="Click me", fg="red", command=clicked)

btn.grid(column=1, row=0)

root.mainloop()
