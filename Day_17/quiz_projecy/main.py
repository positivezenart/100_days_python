from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

""" quiz program"""
question_bank =[]
for i in range(0,10):
     question_bank.append(Question(question_data[i]['text'],question_data[i]['answer']))


quiz = QuizBrain(question_bank)


while quiz.still_has_question():
       quiz.next_question()
       

if quiz.still_has_question() != True:
   print("you have completed the quizz")
   print(f"your final score is {quiz.score}")
   
