from food import *
from turtle import *

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"score = {self.score}",align=ALIGNMENT,font=FONT)
       
    
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def Gameover(self):
        self.goto(0,0)
        self.write(f"Game over",align="center",font=FONT)
        
        
        
    
        