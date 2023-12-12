from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
menu = Menu()
coffeeMaker = CoffeeMaker()

def main():
    print('Welcome to the Coffee Maker')
    is_on = True
    while is_on:
        action = input(f"What would you like? {menu.get_items()}: ")
        if action == "off":
            is_on = False
        elif action == "report":
            coffeeMaker.report()
            moneyMachine.report()
        else:
            order = menu.find_drink(action)
            if coffeeMaker.is_resource_sufficient(order) and moneyMachine.make_payment(order.cost):
                coffeeMaker.make_coffee(order)


if __name__ == "__main__":
    main()