BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

try:
    df =pd.read_csv("Day_32/data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv(f"Day_32/data/french_words.csv")
else:
    df_dict = df.to_dict(orient="records")
    random_word = random.choice(df_dict)

def remove_word():
    df = pd.read_csv(f"Day_32/data/words_to_learn.csv")
    print(df.count())
    df = df.drop(df[df['French'] == random_word['French']].index, axis=0)
    print(df.count())
    df.to_csv(f"Day_32/data/words_to_learn.csv",index=False)

def next_word():
    global random_word,flip_timer,df_dict
    window.after_cancel(flip_timer)
    random_word = random.choice(df_dict)
    canvas.itemconfig(canvas_image,image=my_image_1)
    canvas.itemconfig(word_title,text=random_word['French'],fill="black")
    canvas.itemconfig(language_title,text="French",fill="black")
    flip_timer=window.after(3000,func=flip_card)
   
    
def flip_card():
    canvas.itemconfig(canvas_image,image=my_image_2)
    canvas.itemconfig(word_title,text=random_word['English'], fill="white")
    canvas.itemconfig(language_title,text="English",fill="white")


window=Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)
my_image_1=PhotoImage(file="Day_32\images\\card_front.png")
my_image_2=PhotoImage(file="Day_32\images\\card_back.png")
canvas_image =canvas.create_image(400,263,image=my_image_1)
language_title=canvas.create_text(400,150,text="title",font=("Ariel",40,"italic"))
word_title=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)






right_image = PhotoImage(file="Day_32\images\\right.png")
button_right = Button(image=right_image,highlightthickness=0,command=remove_word)
button_right.grid(column=1,row=1)

wrong_image = PhotoImage(file="Day_32\images\\wrong.png")
button_wrong = Button(image=wrong_image,highlightthickness=0,command=next_word)
button_wrong.grid(column=0,row=1)
next_word()
window.mainloop()
