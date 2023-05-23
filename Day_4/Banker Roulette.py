import random
from random import choice

name = int(input("enter the number of your friends \n"))
list_of_name =[]
for i in range(name):
    name = input("Enter the name \n")
    list_of_name.append(name)
random_number = random.randint(0,len(list_of_name)-1)
print(f"{list_of_name[random_number]} is going to buy the meal today!")
