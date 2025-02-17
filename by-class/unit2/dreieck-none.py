"""
Warum gibt das folgende Programm `None` am Bildschirm aus?
Lösen Sie das Problem.
"""

from turtle import *

def dreieck(a, color):
    pencolor(color)
    for _ in range(3):
        forward(a)
        left(120)

print(dreieck(100, "blue"))
