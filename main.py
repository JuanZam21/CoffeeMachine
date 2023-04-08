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
    "money" : 0,
}

resourcesLeft = []  
end = False  

def report():
    for key in resources:
        print(f"{key}:{resources[key]}")

def enoughResources(drink):    
    for resource in resources:
        for key in MENU[drink]["ingredients"]:
            if MENU[drink]["ingredients"][key] > resources[key]:
                if not key in resourcesLeft:
                    resourcesLeft.append(key)
    output = f"Resources left: "
    if len(resourcesLeft) > 1:
        for i, resource in enumerate(resourcesLeft):
            if i == len(resourcesLeft) - 1:
                output += f"and {resource}."
            else:
                output += f"{resource}, "
        return print(output)  
    elif not resourcesLeft == []:
        output += f"{resourcesLeft[0]}"
        return print(output)
    else:
        return 0

def payment(drink, coins):
    precio = MENU[drink]["cost"]
    if coins < precio:
        return 0
    elif coins == precio:
        resources["money"] += precio
        return 
    elif coins > precio:
        change = round((coins - precio), 2)
        resources["money"] += precio
        return print(f"Here your change: ${change}")

def makeCoffe(drink):
    for resource in resources:
        for key in MENU[drink]["ingredients"]:
            resources[key] = resources[key] - MENU[drink]["ingredients"][key]
        return print(f"here is your {drink}. Enjoy!")
            
while not end:
    
    # prompt the user to input their choice
    choice = input("\n What would you like? (espresso/latte/cappuccino):").lower()
    
    # if the user chooses to turn off the machine, set end flag to True to exit the loop
    if choice == "off":
        end = True
    
    # if the user chooses to get a report, print the current levels of all resources
    elif choice == "report":
        report() 
    
    # if the user chooses to order an espresso, check if there are enough resources
    elif choice:
        eResources = enoughResources(choice)
        if eResources == 0:
            print("Please insert the coins:")
            quartes = int(input("how many quartes? "))
            dimes = int(input("how many dimes? "))
            nickles = int(input("how many nickles? "))
            pennies = int(input("how many pennies? "))
            coins = (quartes*.25 + dimes*.1 + nickles*.05 + pennies*.01)
            if payment(choice, coins) == 0:
                print("Sorry that's not enough money. Money refunded")
            else:
                makeCoffe(choice)