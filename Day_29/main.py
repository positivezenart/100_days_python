from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SYMBOL ="✔"
REPS =0
Timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(Timer)
    labels.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text ="")
    global REPS
    REPS =0
    #timer_text.config(text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS +=1
    WORK_MIN_SECONDS = WORK_MIN * 60
    SHORT_BREAK_MIN_SECONDS = SHORT_BREAK_MIN * 60
    LONG_BREAK_MIN_SECONDS = LONG_BREAK_MIN * 60
    if REPS %8 ==0:
        labels.config(text="Long Break",fg=RED)
        countdown(LONG_BREAK_MIN_SECONDS)
    elif REPS %2 ==0:
        labels.config(text="Short Break" ,fg=RED)
        countdown(SHORT_BREAK_MIN_SECONDS)
    else:
       labels.config(text="Work",fg=GREEN)
       countdown(WORK_MIN_SECONDS)
        
        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes= math.floor(count/60)
    seconds=count%60
    if seconds == 0:
       seconds == "00"
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text,text=f"0{minutes}:{seconds}")
    if count >0:
       global Timer
       Timer =window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark =""
        work_session = math.floow(REPS/2)
        for _ in range(work_session):
            mark += "✔"
        label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomdoro")
# window.minsize(width=600,height=600)
window.config(padx=100.,pady=50,bg=YELLOW)
labels = Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
labels.grid(column=2,row=1)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image_tomato =PhotoImage(file="Day_29\\tomato.png")
canvas.create_image(100,112,image=image_tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


button = Button(text="Start",command=start_timer)
button.grid(column=0,row=3)
button.config(bg="Green", fg="white",width = "9", font=("Arial", 14),borderwidth = '2')
label = Label(text=SYMBOL,fg=GREEN,bg=YELLOW)
label.grid(column=2,row=4)
button = Button(text="End",command=reset_timer)
button.grid(column=3,row=3)
button.config(bg="Green", fg="white",width = "9" ,font=("Arial", 14),   borderwidth = '2')
window.mainloop()