from turtle import Turtle,Screen

import random

number_of_colors = 12

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]


t = Turtle()
""" Trying to create a gemotricala agnle"""
def shape_maker(n):
    for i in range(n):
        angle = 360 /n
        t.forward(100)
        t.right(angle)

def pyRandColor():
    randNums = [random.random() for _ in range(0, 3)]

    RGB255 = list([ int(i * 255) for i in randNums ])
    RGB1 = list([ round(i, 2) for i in randNums ])
    return RGB1
        

for shape_in_size in range(3,11):
        shape_maker(shape_in_size)
        t.color(pyRandColor())
    



screen = Screen()
screen.exitonclick()
