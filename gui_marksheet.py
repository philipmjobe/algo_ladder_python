# Create a python GUI mark sheet. Where credits of each subject are given, enter the grades obtained in each subject and click on Submit. The credits per subject, the total credits as well as the SGPA are displayed after being calculated automatically. Use Tkinter to create the GUI interface.

import tkinter as tk

master = tk.Tk()

master.title("MARKSHEET")

master.geometry("700x250")

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)


def display():

    tot = 0

    if e4.get() == "A":
        tk.Label(master, text="40").grid(row=3, column=4)
        tot += 40

    if e4.get() == "B":
        tk.Label(master, text="36").grid(row=3, column=4)
        tot += 36

    if e4.get() == "C":
        tk.Label(master, text="32").grid(row=3, column=4)
        tot += 32

    if e4.get() == "D":
        tk.Label(master, text="28").grid(row=3, column=4)
        tot += 28

    if e4.get() == "P":
        tk.Label(master, text="24").grid(row=3, column=4)
        tot += 24

    if e4.get() == "F":
        tk.Label(master, text="0").grid(row=3, column=4)
        tot += 0
