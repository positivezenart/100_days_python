import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

choice = random. randint(1, 100)

input_value = input("Choose difficultly, Type 'easy' or 'hard': ")

if input_value == 'easy':
   life_left = 10
else:
   life_left = 5


still_have_chance = 0

while still_have_chance < life_left:
    print(f"you have lost {still_have_chance} life")
    guess_the_number = int(input('Make a guess:'))
    if guess_the_number < choice:
        print("Its too low")
        still_have_chance += 1
        if still_have_chance == life_left:
           print(f"you have lost, The number is {choice}")
    elif guess_the_number > choice:
         print("Its too high")
         still_have_chance += 1
         if still_have_chance == life_left:
            print(f"you have lost, The number is {choice}")
    elif guess_the_number == choice:
         print(f"you got it, The number is {choice}")