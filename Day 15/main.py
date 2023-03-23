from coffee import MENU, resources

quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

resource_water = resources["water"]
resource_milk = resources["milk"]
resource_coffee = resources["coffee"]
resource_money = resources["money"]
n1 = "\n"
begin = False


def check_resources(coffee_type):
    if coffee_type == "espresso":
        menu_water = MENU[coffee_type]["ingredients"]["water"]
        menu_coffee = MENU[coffee_type]["ingredients"]["coffee"]
        if resource_water <= menu_water:
            print("Sorry there is not enough water.")
            return False
        elif resource_coffee <= menu_coffee:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    elif coffee_type == "latte":
        menu_water = MENU[coffee_type]["ingredients"]["water"]
        menu_milk = MENU[coffee_type]["ingredients"]["milk"]
        menu_coffee = MENU[coffee_type]["ingredients"]["coffee"]
        if resource_water <= menu_water:
            print("Sorry there is not enough water.")
            return False
        elif resource_coffee <= menu_coffee:
            print("Sorry there is not enough coffee.")
            return False
        elif resource_milk <= menu_milk:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    elif coffee_type == "cappuccino":
        menu_water = MENU[coffee_type]["ingredients"]["water"]
        menu_milk = MENU[coffee_type]["ingredients"]["milk"]
        menu_coffee = MENU[coffee_type]["ingredients"]["coffee"]
        if resource_water <= menu_water:
            print("Sorry there is not enough water.")
            return False
        elif resource_coffee <= menu_coffee:
            print("Sorry there is not enough coffee.")
            return False
        elif resource_milk <= menu_milk:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True


def process_coins(coffee_type, quarters, dimes, nickles, pennies):
    menu_cost = MENU[coffee_type]["cost"]
    quarter1 = quarters * quarter
    dime1 = dimes * dime
    nickle1 = nickles * nickle
    pennies1 = pennies * penny
    total = quarter1 + dime1 + nickle1 + pennies1
    change = round(total - menu_cost, 2)

    if total < menu_cost:
        return False
    else:
        return True, change


while begin == False:
    user_input = input("Would you like a coffee? Type 'yes' or 'no'. ")
    if user_input == "yes":
        start_machine = True
        begin = True
    elif user_input == "no":
        start_machine = False
        begin = True
    else:
        print("Invalid input, please enter 'yes' or 'no'.")

while start_machine == True:

    correct_coffee = False
    while correct_coffee == False:
        coffee_type = input(
            "What would you like? (Espresso / Latte / Cappuccino): ").lower()

        if coffee_type == "report":
            print(
                f"Water: {resource_water}ml{n1}Milk: {resource_milk}ml{n1}Coffee: {resource_coffee}g{n1}Money: ${resource_money}")
        elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappucino":
            correct_coffee = True
        else:
            print(
                "Invalid Input. Pleas enter 'espresso', 'latte', 'cappucino' or the special word 'report.")

    check = check_resources(coffee_type)
    if check == True:
        print("Please insert coins.")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))

        coins = process_coins(coffee_type, quarters,
                              dimes, nickles, pennies)

        if coins[0] == True and coffee_type == "espresso":
            print(f"Here is ${coins[1]} in change.")
            print(f"Here is your {coffee_type}. Enjoy!")
            resource_money += MENU[coffee_type]["cost"]
            resource_water -= MENU[coffee_type]["ingredients"]["water"]
            resource_coffee -= MENU[coffee_type]["ingredients"]["coffee"]
            stop_machine = False
        elif coins[0] == True and coffee_type == "latte" or coffee_type == "cappuccino":
            print(f"Here is ${coins[1]} in change.")
            print(f"Here is your {coffee_type}. Enjoy!")
            resource_money += MENU[coffee_type]["cost"]
            resource_water -= MENU[coffee_type]["ingredients"]["water"]
            resource_milk -= MENU[coffee_type]["ingredients"]["milk"]
            resource_coffee -= MENU[coffee_type]["ingredients"]["coffee"]
            stop_machine = False
        elif coins[0] == False:
            print("Sorry that's not enough money. Money refunded.")
            stop_machine = False
        else:
            stop_machine = False

    stop_machine = False

    while stop_machine == False:
        last_input = input("Would you like a coffee? Type 'yes' or 'no'. ")
        if last_input == "yes":
            stop_machine = True
            correct_coffee = False
        elif last_input == "no":
            stop_machine = True
            start_machine = False
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
