# turtle is an inbuilt module in Python. It provides drawing using a screen (cardboard) and turtle (pen). To draw something on the screen, we need to move the turtle (pen). To move turtle, there are some functions i.e forward(), backward(), etc.

# DRAWING A SQUARE

import turtle

# t = turtle.Turtle()

# s = int(input("Enter the length of the side of the Square: "))

# t.forward(s)
# t.left(90)

# t.forward(s)
# t.left(90)

# t.forward(s)
# t.left(90)

# t.forward(s)
# t.left(90)

# DRAWING A SQUARE USING A LOOP

# t = turtle.Turtle()

# s = int(input("Enter the length of the side of the square: "))

# for _ in range(4):
#     t.forward(s)
#     t.left(90)

# DRAWING A RECTANGLE

t = turtle.Turtle()

l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))

t.forward(l)
t.left(90)

t.forward(w)
t.left(90)

t.forward(l)
t.left(90)

t.forward(w)
t.left(90)
