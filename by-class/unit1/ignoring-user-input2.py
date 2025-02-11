"""
- Why does the following code does not consider the triangle size entered by the user?
- What must be changed to resolve this issue?
"""

from turtle import *

länge = input("Wie gross soll das Dreieck sein? ")
länge = int(länge)

forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)

pensize(5)
pencolor("red")

exitonclick()
