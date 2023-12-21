from turtle import Turtle,Screen
import random

is_race_on = False
s = Screen()
s.setup(width=500,height=400)
user_bet =s.textinput(title="Question", prompt ="which turtle will win the race?")

color =["red", "green", "yellow", "blue", "orange", "black"]

destionation =[-10,-70,-40,25,50,80]

all_turtles =[]

if user_bet:
   is_race_on = True
   

for i in range(0,6):
    t1 = Turtle(shape = "turtle")
    t1.color(color[i])
    t1.penup()
    t1.goto(x=-230,y = destionation[i])
    all_turtles.append(t1)
    
while is_race_on:
      for turtle in all_turtles:
          if turtle.xcor() > 230:
             winning_color = turtle.pencolor()
             if user_bet == winning_color:
                print(f"Your {winning_color} has won the race \n")
                is_race_on = False
             else:
                 print(f"{winning_color} has won the race")
                 print("sorry, you have lose the race")
                 is_race_on = False
          else:   
             rand_distance = random.randint(0,10)
             turtle.forward(rand_distance)
          



s.listen()
s.exitonclick()