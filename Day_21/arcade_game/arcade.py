from turtle import Screen,Turtle


class Arcade(Turtle):
    def __init__(self,position):
        super().__init__()
        self.screen_create()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)

    
    def screen_create(self): #creating a screen
        screen = Screen()
        screen.setup(width = 800, height = 600)
        screen.bgcolor("black")
        screen.title("Pong")
        screen.tracer(0) 

    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)