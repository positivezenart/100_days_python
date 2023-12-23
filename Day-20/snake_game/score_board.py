from food import *
from turtle import *

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')

with open("Day-20\snake_game\score.txt", encoding="utf-8",mode = "r") as f:
    HIGHEST_SCORE = f.read()


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGHEST_SCORE)
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self): #disply scoreson board
        self.clear()
        self.write(f"score = {self.score} high_score = {self.high_score}",align=ALIGNMENT,font=FONT)
        
    def rest_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("Day-20\snake_game\score.txt", encoding="utf-8",mode = "w") as f:
             f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
       
    
    def increaseScore(self): #update the score and clear it everytime
        self.score += 1
        self.update_scoreboard()
     
    # def Gameover(self): #to disaply game over message
    #     self.goto(0,0)
    #     self.write(f"Game over",align="center",font=FONT)
        
        
        
    
        