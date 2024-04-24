from turtle import *
a=Turtle()
sides=6
length=70
angle=360.0/sides
for i in range(sides):
    a.forward(length)
    a.right(angle)