MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#declarte the values of each money parameters
quarters = 0.25 
dimes = 0.10
nickles = 0.05
pennies = 0.01


def paid_money(*kwargs):
    print("Please insert coins")
    quarters_value = int(input("How many quarters?"))
    dimes_value = int(input("How many dimes?"))
    nickles_value = int(input("how many nickles?"))
    pennies_value = int(input("how many pennies?"))
    paid_amount = quarters_value * quarters + dimes_value * dimes + nickles_value * nickles + pennies_value * pennies
    return paid_amount

def coffe_preparion(*kwargs):
    global machine_profit
    if paid_amount >=  MENU[coffee_choice]['cost'] :
       machine_profit += MENU[coffee_choice]['cost']
       if paid_amount > MENU[coffee_choice]['cost']:
          change = paid_amount - MENU[coffee_choice]['cost']
          print(f"Here's your changes ! {change}")
          print(f" Enjoy your {coffee_choice} ❤️, Enjoy!")
       else:
          print(f" Enjoy your {coffee_choice} ❤️, Enjoy!")                          
    else:
          print("Sorry thats not enough money to buy this coffee 😒, Money refunded")
           
    

is_it_running = True
machine_profit = 0

while is_it_running:
      coffee_choice = input("What would you like: ? (espresso/latte/cappuccino)")
      machine_property = input("Do you need report or want to switch off?, (off/yes/report)")
      if machine_property != "off" and machine_property != "report":
        paid_amount = paid_money()
        if coffee_choice == 'espresso':
           coffe_preparion()
        elif coffee_choice == 'latte':
           coffe_preparion()    
        elif coffee_choice == 'cappuccino':
           coffe_preparion()
      elif machine_property == "report":
          resources['profit'] = machine_profit
          print(f"profit made by machine {resources}")  
      else: 
          print(machine_profit)
          is_it_running = False
    
        

