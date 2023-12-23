from turtle import *

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    
    def update_scoreboard(self): #disply scoreson board
        self.goto(-100,200)
        self.write(f"l_score = {self.l_score}",align=ALIGNMENT,font=FONT)
        self.goto(100,200)
        self.write(f"r_score = {self.r_score}",align=ALIGNMENT,font=FONT)
    
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()
    