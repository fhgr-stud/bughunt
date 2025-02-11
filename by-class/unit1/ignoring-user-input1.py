"""
- Why does the following code does not consider the triangle size entered by the user?
- What must be changed to resolve this issue?
"""

from turtle import *

länge = input("Wie gross soll das Dreieck sein? ")
länge = int(100)

forward(länge)
left(120)
forward(länge)
left(120)
forward(länge)
left(120)

pensize(5)
pencolor("red")

exitonclick()
