from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
cash_register = MoneyMachine()

is_running = True

while is_running:
    current_menu = menu.get_items().strip("/")
    user_order = input(f"What would you like? ({current_menu})\n").lower()
    if user_order == "off":
        is_running = False
    elif user_order == "report":
        coffee_maker.report()
        cash_register.report()
    else:
        user_order = menu.find_drink(user_order)
        if user_order:
            if coffee_maker.is_resource_sufficient(
                user_order
            ) and cash_register.make_payment(user_order.cost):
                coffee_maker.make_coffee(user_order)