import random
from random_word import RandomWords
from hangman_art import *
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#generated a random word
r = RandomWords()
choosen_word= r.get_random_word()
print(choosen_word)

word_length = len(choosen_word)
print(word_length)


empty_list =[]

for i in range(word_length):
    empty_one = "_"
    empty_list.append(empty_one)
print(empty_list)

lives = 6
end_game = False
while not end_game:
      print(f"you are left with two {lives} lives")
      if lives > 0:
         guess_letters =input("Guess Letter: ? \n").lower()
         for i in range(word_length):
            if choosen_word[i] == guess_letters:
                  empty_list[i] = guess_letters
                  print(empty_list)
      if guess_letters not in choosen_word:
         lives -= 1 
         print(stages[lives])
      if lives == 0:
         print("you lost")
         break 
      if "_" not in empty_list:
         end_game = True
         print(empty_list)
         print("you Win")
      
         


