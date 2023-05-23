print("Welcome to Treasure Island.Your mission is to find the treasure.")
asci_values = ''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 '''
print(asci_values)

direction = input("do you want to go left or right direction? \n")

if direction == 'left':
    next_step = input("do you want to swim or wait?")
    if next_step == 'wait':
        door = input("Open anyone of the door,(red,yellow,blue)")
        if door == 'red':
            print("burned by the fire")
            print("game over")
        elif door == 'yellow':
            print("you have found the treasure")
            print("you win")
        elif door == 'blue':
            print('Eaten by beasts')
            print('game over')
        else:
            print("game over")        
    else:
       print("Attacked by trout")
       print("game over")
else:
    print("Fall into a hole")
    print("game over")