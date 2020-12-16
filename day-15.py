from day_15_menu import *
import os

quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01
earnings = 0.0
available = True


def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry not enought {item}")
            return False
    return True

def make_coffee(coffee, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


while available:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Profit: ${earnings}")

    elif order == 'off':
        available = False
        os.system('clear')

    elif order in MENU:
        print("Insert coins")
        total = int(input("How many quarters: ")) * 0.25
        total += int(input("How many dimes: ")) * 0.1
        total += int(input("How many nickels: ")) * 0.05
        total += int(input("How many pennies: ")) * 0.01

        if total >= MENU[order]['cost'] and enough_resources(MENU[order]['ingredients']):
            change = round(total - MENU[order]['cost'], 2)
            if change == 0:
                print('No change')

            print(f"Here is {change} in change")
            earnings += MENU[order]['cost']

            make_coffee(order, MENU[order]['ingredients'])

        else:
            print("Sorry not enough money. Refunded!")
    else:
        print("Try Again.")
