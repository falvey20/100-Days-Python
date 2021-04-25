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

# money declared globally.
money = 0


# report prints amount of each resource and money
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# Takes drink_ingredients and iterates through each ingredient.
# Returns false is drink ingredient is higher than corresponding resource ingredient.
def check_resources(drink_ingredients):
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


def process_coins():
    print("Please insert coins.")
    balance = int(input("how many quarters?: ")) * 0.25
    balance += int(input("how many dimes?: ")) * 0.1
    balance += int(input("how many nickles?: ")) * 0.05
    balance += int(input("how many pennies?: ")) * 0.01
    return balance


# Iterates through ingredients for chosen drink.
# Deducts drink ingredient volume from resources for corresponding ingredient.
def make_coffee(drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]


def coffee_machine():
    coffee_machine_on = True
    # As long as machine is on, ask what user would like.
    while coffee_machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # Secret commands for report and off.
        if choice == "report":
            report()
        elif choice == "off":
            coffee_machine_on = False
        else:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                balance = process_coins()

                if balance < MENU[choice]["cost"]:
                    print("Sorry that's not enough money, money refunded.")
                else:
                    make_coffee(drink["ingredients"])
                    drink_cost = drink["cost"]
                    global money
                    money += drink["cost"]
                    change = round(balance - drink_cost, 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                        print(f"Here is your {choice}. Enjoy!")


# Call coffee_machine function
coffee_machine()
