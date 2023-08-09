from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_done = False
while not is_done:
    coffees = menu.get_items()
    coffee_choice = input(f"Choose a coffee: {coffees} ").lower()

    if coffee_choice == 'off':
        is_done = True
    elif coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
