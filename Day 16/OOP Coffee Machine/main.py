from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


is_on = True

while is_on:

    choice = input("​What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            money.make_payment(drink.cost)
            coffee.make_coffee(drink)
