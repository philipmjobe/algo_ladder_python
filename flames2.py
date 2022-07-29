# Let’s create a GUI version of a simple FLAMES game.FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. This game does not accurately predict whether an individual is right for you, but it can be fun to play this with your friends.

from tkinter import *


def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]

                list1.remove(c)
                list2.remove(c)

                list3 = list1 + ["*"] + list2

                return [list3, True]

    list3 = list1 + ["*"] + list2
    return [lsit3, False]
