MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 400,
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
    "coffee": 10,
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
        for resource in resources:
            for key in MENU["espresso"]["ingredients"]:
                if MENU["espresso"]["ingredients"][key] > resources[key]:
                    print(key)
                 



                          
            