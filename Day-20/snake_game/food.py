from turtle import Turtle
import random
class Food(Turtle): 
       
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    
    def refresh(self): #display food everythime in different place when its refreshed
        randx = random.randint(-280,280)
        randy = random.randint(-280,280)
        self.goto(randx,randy)
        