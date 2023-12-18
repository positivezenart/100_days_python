from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

My_Money_Machine = MoneyMachine()
Coffee_Maker = CoffeeMaker()
menu_item = Menu()


is_on = True
while is_on:
     options = menu_item.get_items()
     choice = input(f"What would you like: ? {options}")
     if choice == 'off':
         is_on = False
     elif choice == 'report':
         My_Money_Machine.report()
         Coffee_Maker.report()
     else:
        drink = menu_item.find_drink(choice)
        if Coffee_Maker.is_resource_sufficient(drink) and My_Money_Machine.make_payment(drink.cost):
            Coffee_Maker.make_coffee(drink)
            
         
     
