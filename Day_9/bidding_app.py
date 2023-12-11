from art import *
print(logo)
print("Welcome to the bidding syste")
empty_dictionary = {}
while True:
    Name = input("whats your name? \n").lower()
    bid = int(input("whats your bid amount? \n"))
    
    empty_dictionary[Name] = bid
    continue_play = input(" is there any other users want to bid yes or no? \n").lower()
    if continue_play == "no":
        highest_value = 0
        for i,j in empty_dictionary.items():
             if j > highest_value:
                highest_value = j
                final_winner = i
        print(f"Highest {highest_value} $ bid is done by {final_winner},he is the winner")
        break
    else:
        continue

