"""
The triangle is always drawn with the same size.
Why does the program ignore the user input? How can we correct the program?
"""

from turtle import *

input("Triangle size: ")
size = 10

pencolor("red")
forward(size)
left(120)
forward(size)
left(120)
forward(size)
left(120)
exitonclick()
