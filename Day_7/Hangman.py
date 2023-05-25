import random
from random_word import RandomWords
#generated a random word
r = RandomWords()
random_word= r.get_random_word()
print(random_word)

life_line = 0
letter=str()
while  life_line < 7:
       guess_the_word = input("guess the letter of the word \n").lower()
       if guess_the_word in random_word:
          letter += guess_the_word
       else:
          life_line =life_line + 1
      
if life_line == 0:
    print("gameover")


