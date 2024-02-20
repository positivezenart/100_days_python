from turtle import Turtle,Screen
import pandas as pd

""" Create a game to guess the states"""

df = pd.read_csv(f"Day_26\states.csv")
all_states = df.state.to_list()

def convert_to_title_case(guess):
  """Converts a guess to title case."""
  return guess.title()

screen = Screen()
ti = Turtle()
screen.title("US States game")
image = 'Day_26\\blank_states_img.gif'
screen.addshape(image)
ti.shape(image)


t =Turtle()
t.color("black")
guesed_state_list = list()
total_guessed_state = 0

while total_guessed_state < 50:
    answer_state = screen.textinput(title=f"{len(guesed_state_list)}/50 Guessed states", prompt ="what is the state name?")
    guessed_state = convert_to_title_case(answer_state)
    if guessed_state == "Exit":
       remaining_states =[state for state in all_states if state not in guesed_state_list]
       df_remaining_states = pd.DataFrame(remaining_states,columns=["state"])
       df_remaining_states.to_csv(r'D:\Downloads\100_days_python\Day_26\remainingstates.csv')
       break
    if guessed_state in all_states:
        if guessed_state not in guesed_state_list:
            df_state = df[df["state"] == guessed_state]
            t.penup()
            t.goto(df_state.iloc[0,1],df_state.iloc[0,2])
            t.write(guessed_state, align="center") 
            t.pendown()
            total_guessed_state +=1
            guesed_state_list.append(guessed_state)
    else:
        t.hideturtle()

     