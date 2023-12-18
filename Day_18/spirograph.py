from turtle import *
import random

t = Turtle()
s = Screen()
s.colormode(255)
t.speed(20)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255) 
    return (r,g,b)

for i in range(1,100):
    t.color(random_color())
    t.circle(100)
    t.right(5)
    
s.exitonclick()
    