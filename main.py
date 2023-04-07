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

profit = 0
resources = {
    "water": 30,
    "milk": 20,
    "coffee": 10,
}

resourcesLeft = []  
end = False  

def enoughResources(drink):    
    for resource in resources:
        for key in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][key] > resources[key]:
                if not key in resourcesLeft:
                    resourcesLeft.append(key)
                print(resourcesLeft)
            else:
                return print("Todos los recursos completos")
    output = f"Resources left: "
    for i, resource in enumerate(resourcesLeft):
        if i == len(resourcesLeft) - 1:
            output += f"and {resource}."
        else:
            output += f"{resource}, "
    return print(output)
            

while not end:
    
    # prompt the user to input their choice
    choice = input("\n What would you like? (espresso/latte/cappuccino):").lower()
    
    # if the user chooses to turn off the machine, set end flag to True to exit the loop
    if choice == "off":
        end = True
    
    # if the user chooses to get a report, print the current levels of all resources
    elif choice == "report":
        for key in resources:
            print(f"{key}:{resources[key]}")
    
    # if the user chooses to order an espresso, check if there are enough resources
    elif choice == "espresso":
        enoughResources(choice)

        # create an output string with the depleted resources
        