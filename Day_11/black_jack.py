from art import *
import random 
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card(cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_number = random.choice(cards)
    return cards_number

def sum_cards(player_cards,computer_cards):
    user_sum = sum(player_cards)
    computer_sum = sum(computer_cards)
    return user_sum, computer_sum

def calculate_score(player_cards,computer_cards,user_sum, computer_sum):
    if 11 in computer_cards:
        if computer_sum >= 21:
            return 0
    elif 11 in player_cards:
        if user_sum == 21:
            return 1
    elif user_sum > 21:
        if 11 in player_cards:
           player_cards.remove(11)
           player_cards.append(1)
           user_sum, computer_sum = sum_cards(player_cards,computer_cards)
           if user_sum > 21:
               return 2
        else:
            return 2
    else:
        print(player_cards)
        draw_another_card = input(" do you want to draw another card?(yes/no)")
        return draw_another_card

computer_cards =[]
player_cards =[]
for i in range(0, 2):
    computer_cards.append(random_card(cards))
    player_cards.append(random_card(cards))
print(f"Player cards are{player_cards},computer cards are {computer_cards}")


user_sum, computer_sum = sum_cards(player_cards,computer_cards)
print(f"user sum are {user_sum}, computer sum are {computer_sum}")

    
is_condition = True
while is_condition:
    output  = calculate_score(player_cards,computer_cards,user_sum, computer_sum)
    if output == 0 or output == 1:
       print("you win!")
       is_condition = False
    elif output == 2:
       print("you lose")
       is_condition = False
    elif output == 'yes':
        player_cards.append(random_card(cards))
        continue
    elif output == 'no':
        print(computer_sum)
        print(computer_cards)
        while computer_sum < 17:
                computer_cards.append(random_card(cards))
                user_sum, computer_sum = sum_cards(player_cards,computer_cards)
        if computer_sum > 21:
            print('you have won')
            is_condition = False
        else:
            if sum(player_cards) > sum(computer_cards): 
                       print("you win")
                       is_condition = False
            elif sum(player_cards) == sum(computer_cards):
                       print("draw")
                       is_condition = False
            else:
                       print("you lose")
                       is_condition = False
    