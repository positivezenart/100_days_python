
from turtle import Turtle,Screen
STARTING_POSITION = [(0,0),(-20,0),(-40,0)] #constant should be capital
MOVE_STEPS = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT= 0

class Snake:
    
    def __init__(self):
        self.seg_ments =[]
        self.screen_create()
        self.snake_creation()
        self.head = self.seg_ments[0]
    
    def screen_create(self):
        screen = Screen()
        screen.setup(width = 600, height = 600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)   
    
    def snake_creation(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    
    def add_segment(self,position):
            t1 = Turtle(shape='square')
            t1.pensize(2)
            t1.color("white")
            t1.penup()
            t1.goto(position)
            self.seg_ments.append(t1)
    
    def extend(self):
        self.add_segment(self.seg_ments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.seg_ments)-1,0,-1): #start #stop #step
            new_x = self.seg_ments[seg_num-1].xcor()
            new_y = self.seg_ments[seg_num-1].ycor()
            self.seg_ments[seg_num].goto(new_x,new_y)
        self.seg_ments[0].forward(MOVE_STEPS)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)
        
        