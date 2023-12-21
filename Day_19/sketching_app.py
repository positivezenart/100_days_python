from turtle import Turtle,Screen

t = Turtle()
s = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_backward_left():
    t.left(10)

def move_backward_right():
    t.right(10)

def turtle_clear():
    t.clear()
    t.penup()
    t.home()

s.listen()
s.onkey(key= "w",fun= move_forward)
s.onkey(key= "s",fun= move_backward)
s.onkey(key= "l",fun= move_backward_left)
s.onkey(key= "r",fun= move_backward_right)
s.onkey(key= "space",fun= turtle_clear)
s.exitonclick()