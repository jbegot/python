
def main():

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

    money = 0.0

    while True:
        command = input("What would you like? (espresso/latte/cappuccino):")

        if command == "off":
            print("Turning machine off")
            break

        elif command == "report":
            print_report(resources, money)

        elif command in MENU:
            print(f"{command} chosen.")
            if check_resources(command, resources, MENU):
                money, success = process_transaction(process_coins(command, MENU), command, resources, MENU, money)
                if success:
                    resources = make_order(command, resources, MENU)
                    print(f"Here is your {command}. Enjoy!")

        else:
            print("Not a valid option")
def check_resources(drink_order, resources, MENU):

    for resource in MENU[drink_order]["ingredients"]:
        if resources[resource] < MENU[drink_order]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}")
            return False

    return True

def process_coins(drink_order, MENU):

    print(f"Cost is ${MENU[drink_order]['cost']}. \nInsert coins")
    quarter_count = int(input('Quarters: '))
    nickle_count = int(input('Nickles: '))
    dime_count = int(input('Dimes: '))
    penny_count = int(input('Pennies: '))

    return quarter_count * 0.25 + nickle_count * 0.1 + dime_count * 0.05 + penny_count * 0.01
def process_transaction(amount_given, drink_order, resources, MENU, money):

    if amount_given < MENU[drink_order]['cost']:
        print("“Sorry that's not enough money. Money refunded.")
        success = False
    else:

        # add cost to money stored
        money += MENU[drink_order]['cost']

        # Check for change
        if amount_given > MENU[drink_order]['cost']:
            print(f"Here is ${round(amount_given - MENU[drink_order]['cost'], 2)} in change")

        success = True

    return money, success
def make_order(drink_order, resources, MENU):

    for resource in MENU[drink_order]['ingredients']:
        resources[resource] -= MENU[drink_order]['ingredients'][resource]

    return resources
def print_report(resources, money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")







    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# TODO: 1. Print report of all coffee machine resources

# TODO 2. Check resources sufficient?

# TODO 3. Process coins.

# TODO 4. Check transaction successful?

# TODO 5. Make Coffee