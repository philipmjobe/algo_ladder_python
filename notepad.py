# Let’s see how to create a simple notepad in Python using Tkinter. This notepad GUI will consist of various menu like file and edit, using which all functionalities like saving the file, opening a file, editing, cut and paste can be done.

# Now for creating this notepad, Python 3 and Tkinter should already be installed in your system. You can download suitable python package as per system requirement. After you have successfully installed python you need to install Tkinter (a Python’s GUI package)

import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title("Untitled - Notepad")

        screenWidth = self.__root.winfo_screenmmwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)

        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' %
                             (self.__thisWidth, self.__thisHeight, left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(labe="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(
            label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.
