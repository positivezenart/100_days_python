from turtle import Turtle,Screen

t = Turtle()

for i in range(50):
    if i%2 == 0:
       t.pendown()
       t.forward(5)
    else:
        t.penup()
        t.forward(5)