# Turtle is an inbuilt module of python. It enables us to draw any drawing by a turtle and methods defined in the turtle module and by using some logical loops. turtle drawings are basically drawn using four methods defined in the turtle module.
import turtle

t = turtle.Turtle()

n = int(input("Enter the no if the sides of the polygon : "))
l = int(input("Enter the length of the sides of the polygon : "))

for _ in range(n):
    turtle.forward(1)
    turtle.right(360 / n)
