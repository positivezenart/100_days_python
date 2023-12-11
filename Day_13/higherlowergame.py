#import a modules
from art import *
from game_data import *
import random

print(logo)

#Selecting the random data from list of elements
def random_choice():
    choice = random.randint(1,len(data))
    return data[choice]


is_it_correct = True
current_score = 0
while is_it_correct:
    compare_a = random_choice()
    print(f"Compare A: {compare_a['name']},{compare_a['description']},{compare_a['country']}")
    print(vs)
    compare_b = random_choice()
    print(f"Compare B: {compare_b['name']},{compare_b['description']},{compare_b['country']}")
    choose_value = input("Who has more followers?: 'A' or 'B':")
    if choose_value == 'A':
        if compare_a['follower_count'] > compare_b['follower_count']:
            current_score +=1
            print(f"You are right! , your current score is {current_score}")
            continue
        else:
            print(f"you lost the game, your final score is {current_score}")
            is_it_correct = False
    else:
        if compare_b['follower_count'] > compare_a['follower_count']:
            current_score +=1
            print(f"You are right! , your current score is {current_score}")
            continue
        else:
            print(f"you lost the game, your final score is {current_score}")
            is_it_correct = False
         