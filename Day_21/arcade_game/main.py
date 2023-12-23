from turtle import Turtle ,Screen
from arcade import *
from score_board import *
from ball import *
import time

screen = Screen()
score = ScoreBoard()
Rpaddle = Arcade((350,0))
lpaddle = Arcade((-350,0))
ball = Ball()




screen.listen()
screen.onkey(Rpaddle.go_up,"Up")
screen.onkey(Rpaddle.go_down,"Down")
screen.onkey(lpaddle.go_up,"w")
screen.onkey(lpaddle.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with walls
    
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()
       
    if ball.distance(Rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() > - 320:
        ball.bounce_x()
    

        
    if ball.xcor() > 380 :
       ball.refresh()
       score.l_point()
       
    if ball.xcor() < -380:
       ball.refresh()
       score.r_point()
    

screen.exitonclick()






    










screen.exitonclick()