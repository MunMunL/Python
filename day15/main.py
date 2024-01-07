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


def check_resources(selection):
    """Checks if there is enough resources and prints which resource isn't enough"""
    for item in selection:
        if selection[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """ Adds up all coins inserted and outputs total """
    print("Please insert coins.")
    total =  int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def deduct_resources(selection):
    for item in selection:
        resources[item] -= selection[item]


money = 0
machine_on = True

while machine_on:
    # TODO: 1. Prompt user by asking What would you like? (espresso/latte/cappuccino)
    choice = input("What would you like? (espresso/ latte/ cappuccino): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off" to the prompt.
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: £{money}")

    # TODO: 4. Check resources sufficient?
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            # TODO: 5. Process coins
            total_coins = process_coins()

            # TODO: 6. Check transaction successful?
            cost_choice = (drink["cost"])
            if total_coins < cost_choice:
                print("Sorry that's not enough money.  Money refunded.")
            else:
                money += cost_choice
                change_returned = total_coins - cost_choice
                print(f"Here is £{change_returned:.2f} in change")

            # TODO: 7. Make coffee
                deduct_resources(drink["ingredients"])
                print(f"Here is your {choice} ☕️ . Enjoy!")




