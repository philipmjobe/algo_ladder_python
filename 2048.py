# How to play 2048:

# 1. There is a 4*4 grid which can be filled with any number. Initially two random cells are filled with 2 in it. Rest cells are empty.

# 2. we have to press any one of four keys to move up, down, left, or right. When we press any key, the elements of the cell move in that direction such that if any two identical numbers are contained in that particular row ( in case of moving left or right) or column ( in case of moving up and down) they get add up and extreme cell in that direction fill itself with that number and rest cells goes empty again.

# 3. After this grid compression any random empty cell gets itself filled with 2.

# 4. Following the above process we have to double the elements by adding up and make 2048 in any of the cell. If we are able to do that we wins.

# 5. But if during the game there is no empty cell left to be filled with a new 2, then the game goes over.

# Programming Approach :

# We will design each logic function such as we are performing a left swipe then we will use it for right swipe by reversing matrix and performing left swipe.
# Moving up can be done by taking transpose then moving left.
# Moving down can be done by taking transpose the moving right.
# All the logic in the program are explained in detail in the comments. Highly recommended to go through all the comments.


import logic

if __name__ == '__main__':
    mat = logic.start_game

while(True):
    x = input("Press the command : ")

    if (x == 'W' or x == 'w'):
        mat, flag = logic.move_up(mat)

        status = logic.get_current_state(mat)
        print(status)

        if (status == 'Game Not Over'):
            logic.add_new_2(mat)
        else:
            break

    elif (x == 'S' or x == 's'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if (status == 'Game Not Over'):
            logic.add_new_2(mat)
        else:
            break

    elif (x == 'A' or x == 'a'):
        mat, flag = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if (status == 'Game Not Over'):
            logic.add_new_2(mat)
        else:
            break

    elif (x == 'D' or x == 'd'):
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if (status == 'Game Not Over'):
            logic.add_new_2(mat)
        else:
            break

    else:
        print("Invaild Key Pressed")

    print(mat)
