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
    return [list3, False]


def tell_status():
    p1 = Player1_field.get()
    p1 = p1.lower()
    p1.replace(" ", "")
    p1_list = list(p1)

    p2 = Player2_field.get()
    p2 = p2.lower()
    p2.replace(" ", "")
    p2_list = list(p2)

    proceed = True

    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]