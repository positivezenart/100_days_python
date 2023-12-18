from turtle import Turtle,Screen
import random 
t = Turtle()

t.speed("fastest")
screen = Screen()
screen.colormode(255)
def pyRandColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255) 
    return (r,g,b)

direction = ['left', 'right']
angle = [ 90,-90,-180 ,180,-270, 270]
for i in range(0,300):
    choice = random.choice(direction)
    angles = random.choice(angle)
    t.color(pyRandColor())
    t.pensize(10)
    if choice == 'left':
       t.left(angles)
    else:
       t.right(angles)
    t.forward(50)




screen.exitonclick()
