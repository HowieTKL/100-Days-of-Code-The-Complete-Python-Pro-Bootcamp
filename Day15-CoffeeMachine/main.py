from pdb import test

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

denominations = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}

def check_resources(flavor):
    ingredients = MENU[flavor]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def make_coffee(flavor):
    ingredients = MENU[flavor]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {flavor}")

def insert_money():
    quarters = int(input("Quarters "))
    dimes = int(input("Dimes "))
    nickels = int(input("Nickels "))
    pennies = int(input("Pennies "))
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

profit = 0.0
is_machine_on = True
while is_machine_on:
    action = input("What would you like? (espresso/latte/cappuccino): ")
    if action == "off":
        is_machine_on = False
    elif action == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"money: {profit}")
    elif action == "espresso" or action == "latte" or action == "cappuccino":
        if check_resources(action):
            total = insert_money()
            cost = MENU[action]["cost"]
            if total < cost:
                print("Sorry that's  not enough money. Money refunded.")
            else:
                if total > cost:
                    print(f"Change of {total - cost}")
                make_coffee(action)
                profit += cost
