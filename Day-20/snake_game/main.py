from turtle import Screen
import time
from snake import *
from food import *
from score_board import *

screen = Screen()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
    
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food 
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       score.increaseScore()
       
     #detect collision with   wall
    if snake.head.xcor() >285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
       score.rest_game()
       snake.reset()
        
    #detec collision with  tail
    for segments in snake.seg_ments[1:]:
        if snake.head.distance(segments) < 10:
           score.rest_game()
           snake.reset()

       

screen.exitonclick()