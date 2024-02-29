from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
     def __init__(self,quiz:QuizBrain):
         self.quiz=quiz
         self.window= Tk()
         self.window.title("quizzer")
         self.window.config(padx=20,pady=20,bg=THEME_COLOR)
         self.score_label = Label(text="Score:0",fg="white",bg=THEME_COLOR)
         self.score_label.grid(row=0,column=1)
         self.canvas=Canvas(width=400,height=350,bg="white")
         self.question_text =self.canvas.create_text(200,160,width=200,text="Word",font=("Ariel",20,"italic"),fill=THEME_COLOR)
         self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
         self.right_image = PhotoImage(file="Day_35\quizzler-app-start\images\\true.png")
         self.button_right = Button(image=self.right_image,highlightthickness=0,command=self.true_pressed)
         self.button_right.grid(column=1,row=2)
         self.wrong_image = PhotoImage(file="Day_35\quizzler-app-start\images\\false.png")
         self.button_wrong = Button(image=self.wrong_image ,highlightthickness=0,command =self.false_pressed)
         self.button_wrong.grid(column=0,row=2)
         self.get_next_question()
         self.window.mainloop()
         
     def get_next_question(self):
           self.canvas.config(bg="white")
           q_text= self.quiz.next_question()
           self.canvas.itemconfig(self.question_text,text=q_text)
    
     def true_pressed(self):
         self.give_feedback(self.quiz.check_answer("true"))
         if self.quiz.still_has_questions():
             self.get_next_question()

    
     def false_pressed(self):
         self.quiz.check_answer("false")
         if self.quiz.still_has_questions():
               self.get_next_question()
               
     def give_feedback(self,is_right):
         if is_right:
             self.canvas.config(bg="green")
         else:
             self.canvas.config(bg="red")
             
         self.canvas.after(1000,func=self.get_next_question)
         