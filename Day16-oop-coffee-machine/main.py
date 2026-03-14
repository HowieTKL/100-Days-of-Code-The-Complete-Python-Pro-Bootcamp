from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    action = input(f"What would you like? {menu.get_items()}: ")
    if action == "off":
        is_on = False
    elif action == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)
