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

t = turtle.Turtle()

s = int(input("Enter the length of the side of the square: "))

for _ in range(4):
    t.forward(s)
    t.left(90)
