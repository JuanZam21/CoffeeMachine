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
    "water": 20,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
end = False
while not end:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        end = True
    elif choice == "report":
        for key in resources:
            print(f"{key}:{resources[key]}")
    elif choice == "espresso":
        for key in resources:
            if MENU["espresso"]["ingredients"]["water"] > resources[key]:
                print("Not enought water")
    #print(f"{key_to_compare} in dict1 is bigger than {key_to_compare} in dict2")