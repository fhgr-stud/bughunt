"""
Why do we get a TypeError? How can we correct the program?
"""

from turtle import *

length = input("How large shall I paint the triangle? ")

fillcolor("red")
forward(length)
left(120)
forward(length)
left(120)
forward(length)
left(120)
