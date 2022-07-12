# In this article, we will learn how to create a standard converter using tkinter. Now we are going to create an introduction window that displays loading bar, welcome text, and user’s social media profile links so that when he/she shares his code with some others, they can contact the author using those resources. It looks like a bit lengthy code, but believe me, guys if you start understanding it is so easy and i divided the code into blocks which helps you to understand better.

# Steps to create an introduction window:
# First of all, “Tkinter” and “webbrowser” modules to be imported.
# Create an intro class that fires the introduction window.
# Create a Toplevel Tkinter window in order to use full features of a window.
# Place a welcome label on the top of the window.
# Create one “ttk.Progressbar” which gives us loading effect.
# Finally, create four buttons and provide your social media links using “webbrowser” module.
# And you have to download/create four images to represent your social media links.

from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep
import webbrowser


class intro():

    def __init__(self):
        wind.deiconify()
        wind.resizable(0, 0)
        wind.configure(bg="#008080")
        wind.title("Unit Converter")

        icon = PhotoImage(file=r"convert.png")
        wind.iconphoto(False, icon)

        center(wind, 500, 230)

        entry = Label(wind, bg="#008080", fg="white", text="Welcome to the Unit Converter", font=(
            "Footlight MT Light", 15, "bold"))

        entry.place(x=50, y=30, width=410, height=30)

        self.load = Progressbar(wind, orient=HORIZONTAL,
                                length=250, mode="indeterminate")

        self.start = Button(wind, bg="#f5f5f5", fg="black",
                            text="START", command=self.loading)

        self.start.place(x=200, y=90, width=80, height=30)

        follow = Label(wind, bg="#008080", fg="white",
                       text="Follow Me On", font=("Helvetica", 12, "bold"))

        follow.place(x=186, y=150, width=104, height=20)

        self.git = PhotoImage(file=r'gforg.png')
        github = Button(wind, image=self.git, bg="white", relief=FLAT,
                        command=lambda: self.links("xxxx"), cursor="hand2")

        github.place(x=110, y=190, width=30, height=30)

        self.instag = PhotoImage(file=r'ins.png')
        insta = Button(wind, image=self.instag, bg="#008080", relief=FLAT,
                       command=lambda: self.links("xxxx"), cursor="hand2")

        insta.place(x=190, y=90, width=30, height=30)

        self.fcb = PhotoImage(file=r'fb.png')

        fb = Button(wind, image=self.fcb, bg="white", relief=FLAT,
                    command=lambda: self.links("xxxx"), cursor="hand2")

        fb.place(x=270, y=190, width=30, height=30)

        self.tweet = PhotoImage(file=r'twitter.png')

        twitter = Button(wind, image=self.tweet, bg="white", relief=FLAT,
                         command=lambda: self.links("xxxx"), cursor="hand2")

        twitter.place(x=350, y=190, width=30, height=30)

    def links(self, url):
        webbrowser.get(
            "C:/Program File" + " (x86)/Google/Chrome/Application/chrome.exe" + " %s --incognito").open(url)

    def loading(self):

        self.start.place(x=0, y=0, width=0, height=0)
        self.load.place(x=120, y=100)

        wind.update()

        c = 0

        while(c100):
            shift("Length")


class converter():

    def __init__(self, unit):
        win.deiconify()

        win.resizable(0, 0)
        win.title("Converter")
        icon = PhotoImage(file=r'convert.png')
        win.iconphoto(False, icon)

        center(win, 350, 500)

        self.unit = unit

        upr = Label(win, bg="#add8e6", width=400, height=250)
        upr.place(x=0, y=0)

        lwr = Label(win, bg="#189AB4", width=400, height=250, bd=0)
        lwr.place(x=0, y=0)

        self.menu_lb = Listbox(win, selectmode=SINGLE,
                               height=0, font=("Helvetica", 10))

        self.menu_lb.bind('<>', self.option)

        options = ("", "", "Length", "Temperature", "Speed", "Time", "Mass")

        for i in range(len(options)):
            self.menu_lb.insert(i, options[i])

        self.pic = PhotoImage(file=r"menu.png")
        self.menu = Button(win, image=self.pic, width=35, height=30,
                           bg="#add8e6", bd=0, command=lambda: self.select('m'))

        self.menu.place(x=0, y=0)
