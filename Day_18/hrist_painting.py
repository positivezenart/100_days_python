from turtle import *
from colorgram import *
import random
t= Turtle()
s=Screen()
s.colormode(255)
rgb_colors = []
colors = colorgram.extract('Day_18\image.jpg', 30)
for color in colors:
    r =color.rgb.r
    g =color.rgb.g
    b = color.rgb.b
    random_color = (r,g,b)
    rgb_colors.append(random_color)

t.speed("fastest")
t.penup()
t.setheading(270)
t.forward(300)
t.setheading(0)

for i in range(12):
    for i in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.forward(50)
    
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
       

s.exitonclick()