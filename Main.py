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

def make_drink(drink_type, resources, menu):
    ingredients = menu[drink_type]["ingredients"]
    cost = menu[drink_type]["cost"]

    for ingredient, quantity in ingredients.items():
        if resources[ingredient] < quantity:
            return f"Sorry, there is not enough {ingredient}."

    return cost

def process_coin(coin, cost):
    coin_value = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    total_inserted = sum([coin_value[c] * q for c, q in coin.items()])
    change = round(total_inserted - cost, 2)

    if change < 0:
        return f"Sorry, that's not enough money. Money refunded.", 0
    elif change == 0:
        return "Transaction successful.", 0
    else:
        return f"Here is ${change} in change.", change

def make_coffee(drink_type, resources, menu):
    cost = make_drink(drink_type, resources, menu)
    if isinstance(cost, str):
        return cost

    print(f"The cost of {drink_type} is ${cost}.")
    coin = {
        "quarters": int(input("Quarters: ")),
        "dimes": int(input("Dimes: ")),
        "nickels": int(input("Nickels: ")),
        "pennies": int(input("Pennies: ")),
    }
    result, change = process_coin(coin, cost)
    if change > 0:
        print(result)
    else:
        print(result)
        ingredients = menu[drink_type]["ingredients"]
        for ingredient, quantity in ingredients.items():
            resources[ingredient] -= quantity
        print(f"Here is your {drink_type}. Enjoy!")

def print_report(resources, total_profit):
    print("Report:")
    for resource, quantity in resources.items():
        print(f"{resource.capitalize()}: {quantity}")
    print(f"Money: ${total_profit}")

def main():
    total_profit = 0
    while True:
        print("What would you like? (espresso/latte/cappuccino):")
        drink_type = input().lower()
        if drink_type == "off":
            break
        elif drink_type == "report":
            print_report(resources, total_profit)
        elif drink_type in MENU:
            result = make_coffee(drink_type, resources, MENU)
            if not isinstance(result, str):
                total_profit += result
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
